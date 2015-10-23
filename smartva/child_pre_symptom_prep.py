from __future__ import print_function

import csv
import os

from datetime import date
from dateutil.relativedelta import relativedelta

from smartva.default_fill_data import CHILD_DEFAULT_FILL, CHILD_DEFAULT_FILL_SHORT
from smartva.answer_ranges import CHILD_RANGE_LIST
from smartva.pre_symptom_prep import PreSymptomPrep
from smartva.utils.conversion_utils import additional_headers_and_values, check_skip_patterns, int_value_or_0
from smartva.loggers import status_logger
from smartva.utils import status_notifier, get_item_count
from smartva.child_pre_symptom_data import (
    DURATION_VARS,
    GENERATED_VARS_DATA,
    VAR_CONVERSION_MAP,
    RECODE_MAP,
    FREE_TEXT_VARS,
    SHORT_FORM_FREE_TEXT_CONVERSION,
    BINARY_CONVERSION_MAP,
    SKIP_PATTERN_DATA,
    DURATION_VARS_SPECIAL_CASE,
    DURATION_VARS_SHORT_FORM_DROP_LIST,
    WEIGHT_VARS,
    DATE_VARS,
    EXAM_DATE_VARS,
    DOB_VAR, SEX_VAR,
    WEIGHT_SD_DATA
)
from smartva.word_conversions import CHILD_WORDS_TO_VARS

DROP_PATTERN = '[a]([_\d]|dult)'


# NOTES:
# these variables don't exist in the electronic version of the form:
# c1_09, c1_10, c1_10d, c1_10m, c1_10y, c1_19_6, c1_24, c1_24d, c1_24m, c1_24y, c1_26, c4_31_2, c5_02_11b


class ChildPreSymptomPrep(PreSymptomPrep):
    def __init__(self, input_file, output_dir, short_form):
        PreSymptomPrep.__init__(self, input_file, output_dir, short_form)
        self.AGE_GROUP = 'child'

    def run(self):
        super(ChildPreSymptomPrep, self).run()

        status_logger.info('{} :: Processing pre-symptom data'.format(self.AGE_GROUP.capitalize()))
        status_notifier.update({'progress': 1})

        if self.short_form:
            default_fill = CHILD_DEFAULT_FILL_SHORT
        else:
            default_fill = CHILD_DEFAULT_FILL

        duration_vars = DURATION_VARS[:]

        if self.short_form:
            for var in DURATION_VARS_SHORT_FORM_DROP_LIST:
                duration_vars.remove(var)

        with open(os.path.join(self.output_dir, self.FILENAME_TEMPLATE.format(self.AGE_GROUP)), 'wb') as fo:
            writer = csv.writer(fo)

            with open(self.input_file_path, 'rb') as fi:
                reader = csv.reader(fi)
                records = get_item_count(reader, fi) - 1
                status_notifier.update({'sub_progress': (0, records)})

                headers = next(reader)

                additional_headers_data = GENERATED_VARS_DATA + [(k, '') for k in DURATION_VARS]
                additional_headers, additional_values = additional_headers_and_values(headers, additional_headers_data)

                headers.extend(additional_headers)

                self.rename_headers(headers, VAR_CONVERSION_MAP)

                drop_index_list = self.get_drop_index_list(headers, DROP_PATTERN)
                drop_index_list += self.get_drop_index_list(headers, 'child')
                drop_index_list += [headers.index('{}a'.format(header)) for header in DURATION_VARS]
                drop_index_list += [headers.index('{}b'.format(header)) for header in DURATION_VARS]

                writer.writerow(self.drop_from_list(headers, drop_index_list))

                for index, row in enumerate(reader):
                    if self.want_abort:
                        return False

                    status_notifier.update({'sub_progress': 1})

                    new_row = row + additional_values

                    self.verify_answers_for_row(headers, new_row, CHILD_RANGE_LIST)

                    self.convert_free_text_vars(headers, new_row, FREE_TEXT_VARS, CHILD_WORDS_TO_VARS)

                    if self.short_form:
                        word_list = [v for k, v in SHORT_FORM_FREE_TEXT_CONVERSION.items() if
                                     new_row[headers.index(k)] in [1, '1']]
                        if word_list:
                            self.convert_free_text_words(headers, new_row, word_list, CHILD_WORDS_TO_VARS)

                    self.recode_answers(headers, new_row, RECODE_MAP)

                    self.process_binary_vars(headers, new_row, BINARY_CONVERSION_MAP.items())

                    check_skip_patterns(headers, new_row, SKIP_PATTERN_DATA, default_fill)
                    # special case skip patterns

                    self.calculate_duration_vars(headers, new_row, duration_vars, DURATION_VARS_SPECIAL_CASE)

                    self.validate_weight_vars(headers, new_row)

                    self.process_date_vars(headers, new_row)

                    self.process_weight_sd_vars(headers, new_row)

                    self.fill_missing_data(headers, new_row, default_fill)

                    writer.writerow(self.drop_from_list(new_row, drop_index_list))

    @staticmethod
    def validate_weight_vars(headers, row):
        for var in WEIGHT_VARS:
            if int_value_or_0(row[headers.index(var)]) in [0, 9999]:
                row[headers.index(var)] = ''

    @staticmethod
    def process_date_vars(headers, row):
        # Get an approximate date.
        # Add 'd' (day) 'm' (month) 'y' (years) to each var and process.
        date_invalid = {
            'd': (['', '99', 99], 1),
            'm': (['', '99', 99], 1),
            'y': (['', '999', 999, '9999', 9999], 0),
        }
        for var in DATE_VARS:
            for val, val_data in date_invalid.items():
                var_name = var + val
                invalid_data, default = val_data
                if row[headers.index(var_name)] in invalid_data:
                    row[headers.index(var_name)] = default

    @staticmethod
    def process_weight_sd_vars(headers, row):
        # Get most recent weight from medical records
        if int(row[headers.index('{:s}y'.format(DOB_VAR))]):
            try:
                dob = make_date(headers, row, DOB_VAR)
            except ValueError:
                pass
            else:

                exam_data = []
                for date_var, weight_var in EXAM_DATE_VARS.items():
                    try:
                        exam_date = make_date(headers, row, date_var)
                        exam_weight = float(row[headers.index('{:s}b'.format(weight_var))])
                        exam_data.append((exam_date, exam_weight))
                    except ValueError:
                        # If the date is invalid or the weight isn't a number, skip this exam.
                        continue

                if exam_data:
                    latest_exam, latest_weight = sorted(exam_data, reverse=True)[0]

                    if latest_exam > dob:
                        age_at_exam_months = months_delta(latest_exam, dob)

                        if age_at_exam_months <= 60:
                            sex = int(row[headers.index(SEX_VAR)])
                            weight_kg = latest_weight / 1000

                            for sd_var, sd_data in WEIGHT_SD_DATA.items():
                                row[headers.index(sd_var)] = int(
                                    weight_kg < sd_data.get(sex, {}).get(age_at_exam_months, 0))


def make_date(headers, row, key):
    return date(int(row[headers.index('{:s}y'.format(key))]),
                int(row[headers.index('{:s}m'.format(key))]),
                int(row[headers.index('{:s}d'.format(key))]))


def months_delta(date1, date2):
    delta = relativedelta(date1, date2)
    return abs(delta.years * 12 + delta.months)

"""
# fix child agedays.  if it's blank give it a 0, if it's not, give it a 4
if row[headers.index('c1_25b')] == '' or row[headers.index('c1_25b')] is None:
    row[headers.index('c1_25a')] = '0'
else:
    row[headers.index('c1_25a')] = '4'

if (row[headers.index('c1_25b')] != '' and int(row[headers.index('c1_25b')]) >= 1 and int(
        row[headers.index('c1_25b')]) <= 28):
    row[headers.index('c1_26')] = '1'
"""

"""
# child rash, 4 = days
index = headers.index('c4_33b')
temp = row[headers.index('c4_33a')]
if temp != '4':
    # row[index] = row[headers_old.index('child_4_33a')]
    row[index] = '0'
"""
"""
# added for shortform
if self.short_form:

    # change stools answer from 2 to 1. why?
    index = headers.index('c4_08a')
    temp = row[headers_old.index('child_4_8')]
    if temp == '2':
        row[index] = '1'

    # convert to check skip pattern? {'(c4_07a=1)': ['c4_07b']}
    index = headers.index('c4_07b')
    testval = row[headers.index('c4_07a')]
    if testval != '1':
        row[index] = '0'  # just to make sure that c4_07b doesn't get child_4_7a like in the long form
"""

"""
# Test skip patterns
for i, row in enumerate(matrix):
    # i starts at 0, header row is 1 in excel, so do i+2 for the actual data row

    c3_11 = row[headers.index('c3_11')]
    # This is a unique case because c3_12 can have different 'default' values depending on other variables
    if c1_15 == '1':
        c3_12 = row[headers.index('c3_12')]
        if c3_12 != '0':
            updatestr = 'Child :: Value at row %s col %s for variable c3_12 should be 0, setting to 0 and continuing' % (i + 2, headers.index('c3_12'))
            warning_logger.warning(updatestr)
            row[headers.index('c3_12')] = '0'
    elif c1_26 == '2' or c3_11 == '1':
        c3_12 = row[headers.index('c3_12')]
        if c3_12 != '1':
            updatestr = 'Child :: Value at row %s col %s for variable c3_12 should be 1, setting to default and continuing' % (i + 2, headers.index('c3_12'))
            warning_logger.warning(updatestr)
            row[headers.index('c3_12')] = '1'
    c3_12 = row[headers.index('c3_12')]

"""

"""
# special case: 'child_4_50b' should be set to 1000 if it's missing
for row in matrix:
    if row[headers.index('child_4_50b')] == '' or row[headers.index('child_4_50b')] is None:
        row[headers.index('child_4_50b')] = 1000

"""
