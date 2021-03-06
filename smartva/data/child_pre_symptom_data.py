from smartva.data.common_data import CHILD, MALE, FEMALE
from smartva.data.default_fill_data import CHILD_DEFAULT_FILL, CHILD_DEFAULT_FILL_SHORT
from smartva.data.word_conversions import CHILD_WORDS_TO_VARS

AGE_GROUP = CHILD
DEFAULT_FILL = CHILD_DEFAULT_FILL
DEFAULT_FILL_SHORT = CHILD_DEFAULT_FILL_SHORT
WORDS_TO_VARS = CHILD_WORDS_TO_VARS

KEEP_PATTERN = r'(sid$|g5_|[cn][\d_]|s\d+)'

WEIGHT_VARS = [
    'c5_07_1b',
    'c5_07_2b',
]

DATE_VARS = [
    'g5_01',
    'c5_06_1',
    'c5_06_2',
]

EXAM_DATE_VARS = {
    'c5_06_1': 'c5_07_1',
    'c5_06_2': 'c5_07_2',
}

GENERATED_VARS_DATA = {
    'g4_03b': 0,
    'c1_05b': 0,
    'c1_20b': 0,
    'c1_21b': 0,
    'c2_05b': 0,
    'c4_37b': 0,
    'c4_47_11': 0,
    'c4_49b': 0,
    'c1_25a': 0,
    'c1_26': 0,
    's180': 0,
    's181': 0,
}

VAR_CONVERSION_MAP = {
    'sid': 'sid',
    'gen_2_1': 'g2_01',
    'gen_2_2a': 'g2_02',
    'gen_3_1': 'g3_01',
    'gen_4_2': 'g4_02',
    'gen_4_3': 'g4_03a',
    'gen_4_4': 'g4_04',
    'gen_4_5': 'g4_05',
    'gen_4_6': 'g4_06',
    'gen_4_7': 'g4_07',
    'gen_4_8': 'g4_08',
    'gen_5_1c': 'g5_01d',
    'gen_5_1b': 'g5_01m',
    'gen_5_1a': 'g5_01y',
    'gen_5_2': 'g5_02',
    'gen_5_3c': 'g5_03d',
    'gen_5_3b': 'g5_03m',
    'gen_5_3a': 'g5_03y',
    'gen_5_4a': 'g5_04a',
    'gen_5_4b': 'g5_04b',
    'gen_5_4c': 'g5_04c',
    'gen_5_5': 'g5_05',
    'gen_5_6': 'g5_06a',
    'gen_5_7': 'g5_07',
    'gen_5_8': 'g5_08',
    'child_1_1': 'c1_01',
    'child_1_2': 'c1_02',
    'child_1_3': 'c1_03',
    'child_1_4': 'c1_04',
    'child_1_5': 'c1_05a',
    'child_1_6': 'c1_06a',
    'child_1_6a': 'c1_06b',
    'child_1_7': 'c1_07',
    'child_1_8': 'c1_08a',
    'child_1_8a': 'c1_08b',
    'child_1_11': 'c1_11',
    'child_1_12': 'c1_12',
    'child_1_13': 'c1_13',
    'child_1_14': 'c1_14',
    'child_1_15': 'c1_15',
    'child_1_16': 'c1_16',
    'child_1_17': 'c1_17',
    'child_1_18': 'c1_18',
    'childabnorm1': 'c1_19_1',
    'childabnorm2': 'c1_19_2',
    'childabnorm3': 'c1_19_3',
    'childabnorm4': 'c1_19_4a',
    'child_1_19a': 'c1_19_4b',  # child119a from vaprep
    'childabnorm5': 'c1_19_5',
    'child_1_20': 'c1_20a',
    'child_1_21': 'c1_21a',
    'child_1_22': 'c1_22a',
    'child_1_22a': 'c1_22b',
    'child_1_23': 'c1_23',
    'complications1': 'c2_01_1',
    'complications2': 'c2_01_2',
    'complications3': 'c2_01_3',
    'complications4': 'c2_01_4',
    'complications5': 'c2_01_5',
    'complications6': 'c2_01_6',
    'complications7': 'c2_01_7',
    'complications8': 'c2_01_8',
    'complications9': 'c2_01_9',
    'complications10': 'c2_01_10',
    'complications11': 'c2_01_11',
    'complications12': 'c2_01_12',
    'child_2_2': 'c2_02a',
    'child_2_2a': 'c2_02b',
    'child_2_3': 'c2_03',
    'child_2_4': 'c2_04',
    'child_2_5': 'c2_05a',
    'child_2_6': 'c2_06',
    'child_2_7': 'c2_07',
    'child_2_8': 'c2_08a',
    'child_2_8a': 'c2_08b',
    'child_2_9': 'c2_09',
    'child_2_10': 'c2_10a',
    'child_2_10a': 'c2_10b',
    'child_2_11': 'c2_11',
    'child_2_12': 'c2_12',
    'child_2_15': 'c2_15a',
    'child_2_15a': 'c2_15b',
    'child_2_17': 'c2_17',
    'child_2_18': 'c2_18',
    'child_3_1': 'c3_01',
    'child_3_2': 'c3_02',
    'childabnorm31': 'c3_03_1',
    'childabnorm32': 'c3_03_2',
    'childabnorm33': 'c3_03_3',
    'childabnorm34': 'c3_03_4a',
    'child_3_3a': 'c3_03_4b',
    'childabnorm35': 'c3_03_5',
    'child_3_4': 'c3_04',
    'child_3_5': 'c3_05',
    'child_3_6': 'c3_06',
    'child_3_7': 'c3_07',
    'child_3_8': 'c3_08',
    'child_3_9': 'c3_09',
    'child_3_10': 'c3_10',
    'child_3_11': 'c3_11',
    'child_3_12': 'c3_12',
    'child_3_13': 'c3_13',
    'child_3_14': 'c3_14a',
    'child_3_14a': 'c3_14b',
    'child_3_15': 'c3_15',
    'child_3_16': 'c3_16',
    'child_3_17': 'c3_17',
    'child_3_18': 'c3_18a',
    'child_3_18a': 'c3_18b',
    'child_3_19': 'c3_19a',
    'child_3_19a': 'c3_19b',
    'child_3_20': 'c3_20',
    'child_3_21': 'c3_21a',
    'child_3_21a': 'c3_21b',
    'child_3_22': 'c3_22a',
    'child_3_22a': 'c3_22b',
    'child_3_23': 'c3_23',
    'child_3_24': 'c3_24',
    'child_3_25': 'c3_25',
    'child_3_26': 'c3_26',
    'child_3_27': 'c3_27a',
    'child_3_27a': 'c3_27b',
    'child_3_28': 'c3_28a',
    'child_3_28a': 'c3_28b',
    'child_3_29': 'c3_29',
    'child_3_30': 'c3_30a',
    'child_3_30a': 'c3_30b',
    'child_3_31': 'c3_31a',
    'child_3_31a': 'c3_31b',
    'child_3_32': 'c3_32',
    'child_3_33': 'c3_33',
    'child_3_34': 'c3_34',
    'child_3_35': 'c3_35',
    'child_3_36': 'c3_36',
    'child_3_37': 'c3_37',
    'child_3_38': 'c3_38',
    'child_3_39': 'c3_39',
    'child_3_40': 'c3_40',
    'child_3_41': 'c3_41',
    'child_3_42': 'c3_42',
    'child_3_43': 'c3_43',
    'child_3_44': 'c3_44',
    'child_3_45': 'c3_45a',
    'child_3_45a': 'c3_45b',
    'child_3_46': 'c3_46',
    'child_3_47': 'c3_47',
    'child_3_48': 'c3_48',
    'child_3_49': 'c3_49',
    'child_4_1': 'c4_01',
    'child_4_2': 'c4_02a',
    'child_4_2a': 'c4_02b',
    'child_4_3': 'c4_03',
    'child_4_4': 'c4_04',
    'child_4_5': 'c4_05',
    'child_4_6': 'c4_06',
    'child_4_7': 'c4_07a',
    'child_4_7a': 'c4_07b',
    'child_4_8': 'c4_08a',
    'child_4_8a': 'c4_08b',
    'child_4_9': 'c4_09',
    'child_4_10': 'c4_10a',
    'child_4_10a': 'c4_10b',
    'child_4_11': 'c4_11',
    'child_4_12': 'c4_12',
    'child_4_13': 'c4_13a',
    'child_4_13a': 'c4_13b',
    'child_4_14': 'c4_14',
    'child_4_15': 'c4_15',
    'child_4_16': 'c4_16',
    'child_4_17': 'c4_17a',
    'child_4_17a': 'c4_17b',
    'child_4_18': 'c4_18',
    'child_4_19': 'c4_19a',
    'child_4_19a': 'c4_19b',
    'child_4_20': 'c4_20',
    'child_4_22': 'c4_22',
    'child_4_23': 'c4_23',
    'child_4_24': 'c4_24',
    'child_4_25': 'c4_25',
    'child_4_26': 'c4_26',
    'child_4_27': 'c4_27',
    'child_4_28': 'c4_28',
    'child_4_29': 'c4_29',
    'child_4_30': 'c4_30',
    'child_4_31': 'c4_31_1',
    'child_4_32': 'c4_32',
    'child_4_33': 'c4_33a',
    'child_4_33a': 'c4_33b',
    'child_4_34': 'c4_34',
    'child_4_35': 'c4_35',
    'child_4_36': 'c4_36',
    'child_4_37': 'c4_37a',
    'child_4_38': 'c4_38',
    'child_4_39': 'c4_39',
    'child_4_40': 'c4_40',
    'child_4_41': 'c4_41',
    'child_4_42': 'c4_42',
    'child_4_43': 'c4_43',
    'child_4_44': 'c4_44',
    'child_4_45': 'c4_45',
    'child_4_46': 'c4_46',
    'childinjury1': 'c4_47_1',
    'childinjury2': 'c4_47_2',
    'childinjury3': 'c4_47_3',
    'childinjury4': 'c4_47_4',
    'childinjury5': 'c4_47_5',
    'childinjury6': 'c4_47_6',
    'childinjury7': 'c4_47_7',
    'childinjury8': 'c4_47_8a',
    'child_4_48a': 'c4_47_8b',
    'childinjury10': 'c4_47_9',
    'childinjury9': 'c4_47_10',
    'child_4_49': 'c4_48',
    'child_4_50': 'c4_49a',
    'child_5_1': 'c5_01',
    'provider1': 'c5_02_1',
    'provider2': 'c5_02_2',
    'provider3': 'c5_02_3',
    'provider4': 'c5_02_4',
    'provider5': 'c5_02_5',
    'provider6': 'c5_02_6',
    'provider7': 'c5_02_7',
    'provider8': 'c5_02_8',
    'provider9': 'c5_02_9',
    'provider10': 'c5_02_10',
    'provider11': 'c5_02_11a',
    'provider12': 'c5_02_12',
    'provider13': 'c5_02_13',
    'provider14': 'c5_02_14',
    'child_5_0b': 'c5_0b',
    'child_5_3': 'c5_03',
    'child_5_4': 'c5_04',
    'child_5_5': 'c5_05',
    'child_5_6d': 'c5_06_1d',
    'child_5_6c': 'c5_06_1m',
    'child_5_6b': 'c5_06_1y',
    'child_5_7d': 'c5_06_2d',
    'child_5_7c': 'c5_06_2m',
    'child_5_7b': 'c5_06_2y',
    'child_5_6e': 'c5_07_1a',
    'child_5_6f': 'c5_07_1b',
    'child_5_7e': 'c5_07_2a',
    'child_5_7f': 'c5_07_2b',
    'child_5_8c': 'c5_08d',
    'child_5_8b': 'c5_08m',
    'child_5_8a': 'c5_08y',
    'child_5_9': 'c5_09',
    'child_5_10': 'c5_10',
    'child_5_11': 'c5_11',
    'child_5_12': 'c5_12',
    'child_5_13': 'c5_13',
    'child_5_14': 'c5_14',
    'child_5_15': 'c5_15',
    'child_5_16': 'c5_16',
    'child_5_17': 'c5_17',
    'child_5_18': 'c5_18',
    'child_5_19': 'c5_19',
    'child_6_c': 'c6_01',
    'child_4_47': 'child_4_47',
    'agedays': 'c1_25b',
    'child_6_11': 'c_6_11',
    'child_6_10': 'c_6_10',
    'child_6_9': 'c_6_9',
    'child_6_8': 'c_6_8',
    'child_6_7': 'c_6_7',
    'child_6_6': 'c_6_6',
    'child_6_5': 'c_6_5',
    'child_6_4': 'c_6_4',
    'child_6_3': 'c_6_3',
    'child_6_2': 'c_6_2',
    'child_6_1': 'c_6_1'
}

PROGRESSIVE_VALUE_MAP = {

}

"""
Recode maps use the format:
    (read_header, write_header): {
        VAL: data_header
    }
"""
RECODE_MAP = {
    ('g4_03a', 'g4_03b'): {
        11: 'gen_4_3a',
        12: 'gen_4_3b',
        13: 'gen_4_3c',
    },
    ('c1_05a', 'c1_05b'): {
        4: 'child_1_5a',
        2: 'child_1_5b',
    },
    ('c1_20a', 'c1_20b'): {
        4: 'child_1_20a',
        2: 'child_1_20b',
        1: 'child_1_20c',
    },
    ('c1_21a', 'c1_21b'): {
        4: 'child_1_21a',
        2: 'child_1_21b',
    },
    ('c2_05a', 'c2_05b'): {
        5: 'child_2_5a',
        4: 'child_2_5b',
    },
    ('c4_37a', 'c4_37b'): {
        4: 'child_4_37a',
        3: 'child_4_37b',
    },
    ('c4_49a', 'c4_49b'): {
        5: 'child_4_50a',
        4: 'child_4_50b',
    },
}

BINARY_CONVERSION_MAP = {
    'child_4_47': {
        0: 'c4_47_11',
    },
    'c1_26': '(&(c1_25b>=1)(c1_25b<=28))'
}

SHORT_FORM_FREE_TEXT_CONVERSION = {
    'c_6_1': 'abdomen',
    'c_6_2': 'cancer',
    'c_6_3': 'dehydration',
    'c_6_4': 'dengue',
    'c_6_5': 'diarrhea',
    'c_6_6': 'fever',
    'c_6_7': 'heart',
    'c_6_8': 'jaundice',
    'c_6_9': 'pneumonia',
    'c_6_10': 'rash',
}

FREE_TEXT_VARS = [
    'c1_19_4b',
    'c3_03_4b',
    'c5_0b',
    'c5_09',
    'c5_12',
    'c5_13',
    'c5_14',
    'c5_15',
    'c5_16',
    'c6_01'
]

DURATION_VARS = [
    'c1_05',
    'c1_20',
    'c1_21',
    'c1_25',
    'c2_02',
    'c2_05',
    'c2_10',
    'c3_14',
    'c3_18',
    'c3_19',
    'c3_21',
    'c3_22',
    'c3_27',
    'c3_28',
    'c3_30',
    'c3_31',
    'c4_13',
    'c4_17',
    'c4_19',
    'c4_33',
    'c4_37',
    'c4_49',
]

# These are not scaled, but do check for a unit value of 2
DURATION_DAYS_VARS = [
    'c4_02',
    'c4_08',
    'c4_10',
]

DURATION_VARS_SHORT_FORM_DROP_LIST = []

DURATION_VARS_SPECIAL_CASE = {}

MALE_SD3 = {
    0: 2.1, 1: 2.9, 2: 3.8, 3: 4.4, 4: 4.9, 5: 5.3, 6: 5.7, 7: 5.9, 8: 6.2, 9: 6.4,
    10: 6.6, 11: 6.8, 12: 6.9, 13: 7.1, 14: 7.2, 15: 7.4, 16: 7.5, 17: 7.7, 18: 7.8, 19: 8,
    20: 8.1, 21: 8.2, 22: 8.4, 23: 8.5, 24: 8.6, 25: 8.8, 26: 8.9, 27: 9, 28: 9.1, 29: 9.2,
    30: 9.4, 31: 9.5, 32: 9.6, 33: 9.7, 34: 9.8, 35: 9.9, 36: 10, 37: 10.1, 38: 10.2, 39: 10.3,
    40: 10.4, 41: 10.5, 42: 10.6, 43: 10.7, 44: 10.8, 45: 10.9, 46: 11, 47: 11.1, 48: 11.2, 49: 11.3,
    50: 11.4, 51: 11.5, 52: 11.6, 53: 11.7, 54: 11.8, 55: 11.9, 56: 12, 57: 12.1, 58: 12.2, 59: 12.3,
    60: 12.4
}

FEMALE_SD3 = {
    0: 2, 1: 2.7, 2: 3.4, 3: 4, 4: 4.4, 5: 4.8, 6: 5.1, 7: 5.3, 8: 5.6, 9: 5.8,
    10: 5.9, 11: 6.1, 12: 6.3, 13: 6.4, 14: 6.6, 15: 6.7, 16: 6.9, 17: 7, 18: 7.2, 19: 7.3,
    20: 7.5, 21: 7.6, 22: 7.8, 23: 7.9, 24: 8.1, 25: 8.2, 26: 8.4, 27: 8.5, 28: 8.6, 29: 8.8,
    30: 8.9, 31: 9, 32: 9.1, 33: 9.3, 34: 9.4, 35: 9.5, 36: 9.6, 37: 9.7, 38: 9.8, 39: 9.9,
    40: 10.1, 41: 10.2, 42: 10.3, 43: 10.4, 44: 10.5, 45: 10.6, 46: 10.7, 47: 10.8, 48: 10.9, 49: 11,
    50: 11.1, 51: 11.2, 52: 11.3, 53: 11.4, 54: 11.5, 55: 11.6, 56: 11.7, 57: 11.8, 58: 11.9, 59: 12,
    60: 12.1
}

MALE_SD2 = {
    0: 2.5, 1: 3.4, 2: 4.3, 3: 5, 4: 5.6, 5: 6, 6: 6.4, 7: 6.7, 8: 6.9, 9: 7.1,
    10: 7.4, 11: 7.6, 12: 7.7, 13: 7.9, 14: 8.1, 15: 8.3, 16: 8.4, 17: 8.6, 18: 8.8, 19: 8.9,
    20: 9.1, 21: 9.2, 22: 9.4, 23: 9.5, 24: 9.7, 25: 9.8, 26: 10, 27: 10.1, 28: 10.2, 29: 10.4,
    30: 10.5, 31: 10.7, 32: 10.8, 33: 10.9, 34: 11, 35: 11.2, 36: 11.3, 37: 11.4, 38: 11.5, 39: 11.6,
    40: 11.8, 41: 11.9, 42: 12, 43: 12.1, 44: 12.2, 45: 12.4, 46: 12.5, 47: 12.6, 48: 12.7, 49: 12.8,
    50: 12.9, 51: 13.1, 52: 13.2, 53: 13.3, 54: 13.4, 55: 13.5, 56: 13.6, 57: 13.7, 58: 13.8, 59: 14,
    60: 14.1
}

FEMALE_SD2 = {
    0: 2.4, 1: 3.2, 2: 3.9, 3: 4.5, 4: 5, 5: 5.4, 6: 5.7, 7: 6, 8: 6.3, 9: 6.5,
    10: 6.7, 11: 6.9, 12: 7, 13: 7.2, 14: 7.4, 15: 7.6, 16: 7.7, 17: 7.9, 18: 8.1, 19: 8.2,
    20: 8.4, 21: 8.6, 22: 8.7, 23: 8.9, 24: 9, 25: 9.2, 26: 9.4, 27: 9.5, 28: 9.7, 29: 9.8,
    30: 10, 31: 10.1, 32: 10.3, 33: 10.4, 34: 10.5, 35: 10.7, 36: 10.8, 37: 10.9, 38: 11.1, 39: 11.2,
    40: 11.3, 41: 11.5, 42: 11.6, 43: 11.7, 44: 11.8, 45: 12, 46: 12.1, 47: 12.2, 48: 12.3, 49: 12.4,
    50: 12.6, 51: 12.7, 52: 12.8, 53: 12.9, 54: 13, 55: 13.2, 56: 13.3, 57: 13.4, 58: 13.5, 59: 13.6,
    60: 13.7
}

WEIGHT_SD_DATA = {
    # Standard deviation 3
    's180': {
        # Male
        MALE: MALE_SD3,
        # Female
        FEMALE: FEMALE_SD3,
    },
    # Standard deviation 2
    's181': {
        # Male
        MALE: MALE_SD2,
        # Female
        FEMALE: FEMALE_SD2,
    },
}
