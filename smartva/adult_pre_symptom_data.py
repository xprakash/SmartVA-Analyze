from smartva.common_data import ADULT as AGE_GROUP
from smartva.default_fill_data import (
    ADULT_DEFAULT_FILL as DEFAULT_FILL,
    ADULT_DEFAULT_FILL_SHORT as DEFAULT_FILL_SHORT
)
from answer_ranges import ADULT_RANGE_LIST as RANGE_LIST
from smartva.word_conversions import ADULT_WORDS_TO_VARS as WORDS_TO_VARS

KEEP_PATTERN = r'(sid$|g5_|a_\d+|a\d+_\d|s\d+)'

WEIGHT_VARS = []

DATE_VARS = [
    'g5_01',
]

EXAM_DATE_VARS = {}

GENERATED_VARS_DATA = {
    'g4_03b': 0,
    'a2_01b': 0,
    'a2_22b': 0,
    'a2_24b': 0,
    'a2_26b': 0,
    'a2_28b': 0,
    'a2_33b': 0,
    'a2_37b': 0,
    'a2_41b': 0,
    'a2_54b': 0,
    'a2_58b': 0,
    'a2_62b': 0,
    'a2_65b': 0,
    'a2_68b': 0,
    'a2_70b': 0,
    'a2_73b': 0,
    'a2_76b': 0,
    'a2_79b': 0,
    'a2_83b': 0,
    'a2_86b': 0,
    'a4_02_1': 0,
    'a4_02_2': 0,
    'a4_02_3': 0,
    'a4_02_4': 0,
    'a4_02_5a': 0,
    'a4_02_6': 0,
    'a4_02_7': 0,
    'a5_01_8': 0,
    'a5_04b': '',
    'a6_02_1': 0,
    'a6_02_2': 0,
    'a6_02_3': 0,
    'a6_02_4': 0,
    'a6_02_5': 0,
    'a6_02_6': 0,
    'a6_02_8': 0,
    'a6_02_9': 0,
    'a6_02_10': 0,
    'a6_02_11': 0,
    'a6_02_12a': 0,
    'a6_02_13': 0,
    'a6_02_14': 0,
    'a6_02_15': 0,
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
    'adult_1_1a': 'a1_01_1',
    'adult_1_1b': 'a1_01_2',
    'adult_1_1c': 'a1_01_3',
    'adult_1_1d': 'a1_01_13',
    'adult_1_1e': 'a1_01_5',
    'adult_1_1f': 'a1_01_6',
    'adult_1_1g': 'a1_01_7',
    'adult_1_1h': 'a1_01_8',
    'adult_1_1i': 'a1_01_9',
    'adult_1_1j': 'a1_01_10',
    'adult_1_1k': 'a1_01_11',
    'adult_1_1l': 'a1_01_12',
    'adult_1_1m': 'a1_01_4',
    'adult_1_1n': 'a1_01_14',
    'adult_2_1': 'a2_01a',
    'adult_2_2': 'a2_02',
    'adult_2_3': 'a2_03a',
    'adult_2_3a': 'a2_03b',
    'adult_2_4': 'a2_04',
    'adult_2_5': 'a2_05',
    'adult_2_6': 'a2_06',
    'adult_2_7': 'a2_07',
    'adult_2_8': 'a2_08a',
    'adult_2_8a': 'a2_08b',
    'adultrash1': 'a2_09_1a',
    'adult_2_9a': 'a2_09_1b',
    'adultrash2': 'a2_09_2a',
    'adultrash3': 'a2_09_3a',
    'adult_2_10': 'a2_10',
    'adult_2_11': 'a2_11',
    'adult_2_12': 'a2_12',
    'adult_2_13': 'a2_13',
    'adult_2_14': 'a2_14',
    'adult_2_15': 'a2_15a',
    'adult_2_15a': 'a2_15b',
    'adult_2_16': 'a2_16',
    'adult_2_17': 'a2_17',
    'adult_2_18': 'a2_18',
    'adult_2_19': 'a2_19',
    'adult_2_20': 'a2_20',
    'adult_2_21': 'a2_21',
    'adult_2_22': 'a2_22a',
    'adult_2_23': 'a2_23',
    'adult_2_24': 'a2_24a',
    'adult_2_25': 'a2_25',
    'adult_2_26': 'a2_26a',
    'adult_2_27': 'a2_27',
    'adult_2_28': 'a2_28a',
    'adult_2_29': 'a2_29',
    'adult_2_30': 'a2_30',
    'adult_2_31': 'a2_31',
    'adult_2_32': 'a2_32',
    'adult_2_33': 'a2_33a',
    'adult_2_34': 'a2_34',
    'adult_2_35': 'a2_35',
    'adult_2_36': 'a2_36',
    'adult_2_37': 'a2_37a',
    'adult_2_38': 'a2_38',
    'adult_2_39': 'a2_39_1',
    'adult_2_40': 'a2_40',
    'adult_2_41': 'a2_41a',
    'adult_2_42': 'a2_42',
    'adult_2_43': 'a2_43',
    'adult_2_44': 'a2_44',
    'adult_2_45': 'a2_45',
    'adult_2_46': 'a2_46a',
    'adult_2_46a': 'a2_46b',
    'adult_2_47': 'a2_47',
    'adult_2_48': 'a2_48a',
    'adult_2_48a': 'a2_48b',
    'adult_2_49': 'a2_49',
    'adult_2_50': 'a2_50',
    'adult_2_51': 'a2_51',
    'adult_2_52': 'a2_52',
    'adult_2_53': 'a2_53',
    'adult_2_54': 'a2_54a',
    'adult_2_55': 'a2_55',
    'adult_2_56': 'a2_56',
    'adult_2_57': 'a2_57',
    'adult_2_58': 'a2_58a',
    'adult_2_59': 'a2_59',
    'adult_2_60': 'a2_60',
    'adult_2_61': 'a2_61',
    'adult_2_62': 'a2_62a',
    'adult_2_63': 'a2_63_1',
    'adult_2_64': 'a2_64',
    'adult_2_65': 'a2_65a',
    'adult_2_66': 'a2_66',
    'adult_2_67': 'a2_67',
    'adult_2_68': 'a2_68a',
    'adult_2_69': 'a2_69',
    'adult_2_70': 'a2_70a',
    'adult_2_71': 'a2_71',
    'adult_2_72': 'a2_72',
    'adult_2_73': 'a2_73a',
    'adult_2_74': 'a2_74',
    'adult_2_75': 'a2_75',
    'adult_2_76': 'a2_76a',
    'adult_2_77': 'a2_77',
    'adult_2_78': 'a2_78',
    'adult_2_79': 'a2_79a',
    'adult_2_80': 'a2_80',
    'adult_2_81': 'a2_81',
    'adult_2_82': 'a2_82',
    'adult_2_83': 'a2_83a',
    'adult_2_84': 'a2_84',
    'adult_2_85': 'a2_85',
    'adult_2_86': 'a2_86a',
    'adultparalysis1': 'a2_87_1',
    'adultparalysis2': 'a2_87_2',
    'adultparalysis3': 'a2_87_3',
    'adultparalysis4': 'a2_87_4',
    'adultparalysis5': 'a2_87_5',
    'adultparalysis6': 'a2_87_6',
    'adultparalysis7': 'a2_87_7',
    'adultparalysis8': 'a2_87_8',
    'adultparalysis9': 'a2_87_9',
    'adultparalysis10': 'a2_87_10a',
    'adult_2_87a': 'a2_87_10b',
    'adult_3_1': 'a3_01',
    'adult_3_2': 'a3_02',
    'adult_3_3': 'a3_03',
    'adult_3_4': 'a3_04',
    'adult_3_5': 'a3_05',
    'adult_3_6': 'a3_06',
    'adult_3_7': 'a3_07',
    'adult_3_8': 'a3_08a',
    'adult_3_8a': 'a3_08b',
    'adult_3_9': 'a3_09',
    'adult_3_10': 'a3_10',
    'adult_3_11': 'a3_11a',
    'adult_3_11a': 'a3_11b',
    'adult_3_12': 'a3_12',
    'adult_3_13': 'a3_13',
    'adult_3_14': 'a3_14',
    'adult_3_15': 'a3_15',
    'adult_3_16': 'a3_16a',
    'adult_3_16a': 'a3_16b',
    'adult_3_17': 'a3_17',
    'adult_3_18': 'a3_18',
    'adult_3_19': 'a3_19',
    'adult_3_20': 'a3_20',
    'adult_4_1': 'a4_01',
    'adult_4_2': 'a4_02',
    'adult_4_2a': 'a4_02_5b',
    'adult_4_3a': 'a4_03',
    'adult_4_4a': 'a4_04',
    'adult_4_5': 'a4_05',
    'adult_4_6': 'a4_06',
    'adult_5_1': 'adult_5_1',
    'adultinjury1': 'a5_01_1',
    'adultinjury2': 'a5_01_2',
    'adultinjury3': 'a5_01_3',
    'adultinjury4': 'a5_01_4',
    'adultinjury5': 'a5_01_5',
    'adultinjury6': 'a5_01_6',
    'adultinjury7': 'a5_01_7',
    'adultinjury8': 'a5_01_9a',
    'adult_5_2a': 'a5_01_9b',
    'adult_5_3': 'a5_02',
    'adult_5_4': 'a5_03',
    'adult_5_5': 'a5_04a',
    'adult_6_1': 'a6_01',
    'adult_6_2': 'adult_6_2',
    'adult_6_3': 'a6_03',
    'adult_6_4': 'a6_04',
    'adult_6_5': 'a6_05',
    'adult_6_6d': 'a6_06_1d',
    'adult_6_6c': 'a6_06_1m',
    'adult_6_6b': 'a6_06_1y',
    'adult_6_6h': 'a6_06_2d',
    'adult_6_6g': 'a6_06_2m',
    'adult_6_6f': 'a6_06_2y',
    'adult_6_7c': 'a6_07d',
    'adult_6_7b': 'a6_07m',
    'adult_6_7a': 'a6_07y',
    'adult_6_8': 'a6_08',
    'adult_6_9': 'a6_09',
    'adult_6_10': 'a6_10',
    'adult_6_11': 'a6_11',
    'adult_6_12': 'a6_12',
    'adult_6_13': 'a6_13',
    'adult_6_14': 'a6_14',
    'adult_6_15': 'a6_15',
    'adult_7_c': 'a7_01',
    'adult_7_11': 'a_7_11',
    'adult_7_10': 'a_7_10',
    'adult_7_9': 'a_7_9',
    'adult_7_8': 'a_7_8',
    'adult_7_7': 'a_7_7',
    'adult_7_6': 'a_7_6',
    'adult_7_5': 'a_7_5',
    'adult_7_4': 'a_7_4',
    'adult_7_3': 'a_7_3',
    'adult_7_2': 'a_7_2',
    'adult_7_1': 'a_7_1'
}

"""
Recode map evaluates the read variable and inserts the value of the matching data variable in the write variable.
Format:
    ('read var', 'write var'): {
        VAL: 'data var'
    }
"""
RECODE_MAP = {
    ('g4_03a', 'g4_03b'): {
        11: 'gen_4_3a',
        12: 'gen_4_3b',
        13: 'gen_4_3c',
    },
    ('a2_01a', 'a2_01b'): {
        1: 'adult_2_1a',
        2: 'adult_2_1b',
        4: 'adult_2_1c',
        5: 'adult_2_1d',
    },
    ('a2_22a', 'a2_22b'): {
        4: 'adult_2_22a',
        2: 'adult_2_22b',
    },
    ('a2_24a', 'a2_24b'): {
        4: 'adult_2_24a',
        2: 'adult_2_24b',
    },
    ('a2_26a', 'a2_26b'): {
        4: 'adult_2_26a',
        2: 'adult_2_26b',
    },
    ('a2_28a', 'a2_28b'): {
        4: 'adult_2_28a',
        2: 'adult_2_28b',
    },
    ('a2_33a', 'a2_33b'): {
        4: 'adult_2_33a',
        2: 'adult_2_33b',
    },
    ('a2_37a', 'a2_37b'): {
        4: 'adult_2_37a',
        2: 'adult_2_37b',
    },
    ('a2_41a', 'a2_41b'): {
        4: 'adult_2_41a',
        2: 'adult_2_41b',
    },
    ('a2_54a', 'a2_54b'): {
        5: 'adult_2_54a',
        4: 'adult_2_54b',
    },
    ('a2_58a', 'a2_58b'): {
        4: 'adult_2_58a',
        2: 'adult_2_58b',
    },
    ('a2_62a', 'a2_62b'): {
        5: 'adult_2_62a',
        4: 'adult_2_62b',
        2: 'adult_2_62c',
    },
    ('a2_65a', 'a2_65b'): {
        4: 'adult_2_65a',
        2: 'adult_2_65b',
    },
    ('a2_68a', 'a2_68b'): {
        4: 'adult_2_68a',
        2: 'adult_2_68b',
    },
    ('a2_70a', 'a2_70b'): {
        5: 'adult_2_70a',
        4: 'adult_2_70b',
    },
    ('a2_73a', 'a2_73b'): {
        4: 'adult_2_73a',
        2: 'adult_2_73b',
    },
    ('a2_76a', 'a2_76b'): {
        4: 'adult_2_76a',
        2: 'adult_2_76b',
    },
    ('a2_79a', 'a2_79b'): {
        4: 'adult_2_79a',
        2: 'adult_2_79b',
    },
    ('a2_83a', 'a2_83b'): {
        6: 'adult_2_83a',
        5: 'adult_2_83b',
    },
    ('a2_86a', 'a2_86b'): {
        4: 'adult_2_86a',
        2: 'adult_2_86b',
        1: 'adult_2_86c',
    },
    ('a5_04a', 'a5_04b'): {
        5: 'adult_5_5a',
        4: 'adult_5_5b',
        2: 'adult_5_5c',
        1: 'adult_5_5d',
    },
}

"""
Binary conversion map evaluates the read variable and inserts a 1 for the write variable that matches.
Format:
    'read var' : {
        VAL 1: 'write var 1',
        VAL 2: 'write var 2',
    }
"""
BINARY_CONVERSION_MAP = {
    'a4_02': {
        # old header: adult_4_2
        1: 'a4_02_1',
        2: 'a4_02_2',
        3: 'a4_02_3',
        4: 'a4_02_4',
        11: 'a4_02_5a',
        8: 'a4_02_6',
        9: 'a4_02_7',
    },
    'adult_5_1': {
        # tricky
        0: 'a5_01_8',
    },
    'adult_6_2': {
        # old header: converted
        1: 'a6_02_1',
        2: 'a6_02_2',
        3: 'a6_02_3',
        4: 'a6_02_4',
        5: 'a6_02_5',
        6: 'a6_02_6',
        7: 'a6_02_8',
        8: 'a6_02_9',
        9: 'a6_02_10',
        10: 'a6_02_11',
        11: 'a6_02_12a',
        12: 'a6_02_13',
        88: 'a6_02_14',
        99: 'a6_02_15',
    }
}

"""
Verify that answers are appropriate given answers to previous questions.
Format:
    (answer condition, [list of dependent questions])

Answer condition format:
    (var1=value)     # Data in variable must equal value
    (!(var1=value))  # Data in variable must not equal value
    (&(var1=value)(!(var2=value)))  # Data in var 1 must equal and var 2 must not equal value.
    (|(var1>=value)(!(var2<value))) # Data in var 1 must be greater or equal or var 2 must not be less than value.
    Conditions may be deeply nested:
    (&(|(x1=y1)(x2=y2))(&(x3=y3)(!(x4=y4))))
Note: Instead of making very complex conditions, it may be better to add more dependant questions to smaller conditions.
"""
SKIP_PATTERN_DATA = [
    ('(a2_02=1)', ['a2_03a', 'a2_03b', 'a2_04', 'a2_05', 'a2_06']),
    ('(a2_07=1)', ['a2_08a', 'a2_08b', 'a2_09_1a', 'a2_09_1b', 'a2_09_2a']),
    ('(a2_10=1)', ['a2_11']),
    ('(a2_13=1)', ['a2_14']),
    ('(a2_14=1)', ['a2_15a', 'a2_15b']),
    ('(a2_18=1)', ['a2_19']),
    ('(a2_21=1)', ['a2_22a', 'a2_22b']),
    ('(a2_23=1)', ['a2_24a', 'a2_24b']),
    ('(a2_25=1)', ['a2_26a', 'a2_26b']),
    ('(a2_27=1)', ['a2_28a', 'a2_28b']),
    ('(a2_32=1)', ['a2_33a', 'a2_33b', 'a2_34', 'a2_35']),
    ('(a2_36=1)', ['a2_37a', 'a2_37b', 'a2_38', 'a2_39_1']),
    ('(a2_40=1)', ['a2_41a', 'a2_41b']),
    ('(a2_43=1)', ['a2_44', 'a2_45', 'a2_46a', 'a2_46b']),
    ('(a2_47=1)', ['a2_48a', 'a2_48b']),
    ('(a2_50=1)', ['a2_51']),
    ('(a2_53=1)', ['a2_54a', 'a2_54b', 'a2_55', 'a2_56']),
    ('(a2_57=1)', ['a2_58a', 'a2_58b', 'a2_59']),
    ('(a2_61=1)', ['a2_62a', 'a2_62b', 'a2_63_1']),
    ('(a2_64=1)', ['a2_65a', 'a2_65b', 'a2_66']),
    ('(a2_67=1)', ['a2_68a', 'a2_68b']),
    ('(a2_69=1)', ['a2_70a', 'a2_70b', 'a2_71']),
    ('(a2_72=1)', ['a2_73a', 'a2_73b']),
    ('(a2_74=1)', ['a2_76a', 'a2_76b', 'a2_75', 'a2_77']),
    ('(a2_78=1)', ['a2_79a', 'a2_79b', 'a2_80']),
    ('(a2_82=1)', ['a2_83a', 'a2_83b', 'a2_84']),
    ('(a2_85=1)', ['a2_86a', 'a2_86b', 'a2_87_1', 'a2_87_10a', 'a2_87_10b', 'a2_87_2', 'a2_87_3', 'a2_87_4', 'a2_87_5', 'a2_87_6', 'a2_87_7', 'a2_87_8', 'a2_87_9']),
    ('(a4_01=1)', ['a4_02_1', 'a4_02_2', 'a4_02_3', 'a4_02_4', 'a4_02_5a', 'a4_02_5b', 'a4_02_6', 'a4_02_7']),
    ('(a4_02_1=1)', ['a4_04']),
    ('(a4_05=1)', ['a4_06']),
    ('(!(a5_01_8=1))', ['a5_04a', 'a5_04b', 'a5_02', 'a5_03']),
    ('(!(a5_02=1))', ['a5_03']),
    ('(a6_01=1)', ['a6_02_1', 'a6_02_2', 'a6_02_3', 'a6_02_4', 'a6_02_5', 'a6_02_6', 'a6_02_8', 'a6_02_9', 'a6_02_10', 'a6_02_11', 'a6_02_12a', 'a6_02_13', 'a6_02_14', 'a6_02_15', 'a6_03']),
    ('(a6_04=1)', ['a6_05']),
    ('(a6_05=1)', ['a6_06_1d', 'a6_06_1m', 'a6_06_1y', 'a6_06_2d', 'a6_06_2m', 'a6_06_2y', 'a6_07d', 'a6_07m', 'a6_07y', 'a6_08']),
    ('(a6_09=1)', ['a6_10']),
    ('(a6_10=1)', ['a6_11', 'a6_12', 'a6_13', 'a6_14', 'a6_15']),
    ('(g5_02=2)', ['a3_01', 'a3_02', 'a3_03']),
    ('(&(g5_02=2)(!(a3_03=1)))', ['a3_05', 'a3_06', 'a3_07', 'a3_10']),
    ('(a3_07=1)', ['a3_08a', 'a3_08b', 'a3_09']),
    ('(a3_10=1)', ['a3_11a', 'a3_11b', 'a3_12']),
    ('(&(g5_02=2)(!(a3_03=1))(a3_10=1)(!(a3_12=1)))', ['a3_13', 'a3_14', 'a3_15', 'a3_16a', 'a3_16b']),
    ('(&(g5_02=2)(!(a3_03=1))(!(a3_12=1))(!(a3_15=1)))', ['a3_17']),
    ('(&(g5_02=2)(!(a3_03=1))(!(a3_12=1))(!(a3_15=1))(!(a3_17=1)))', ['a3_18']),
    ('(|(&(g5_02=2)(a3_03=0)(!(a3_15=1))(a3_18=1))(a3_17=1))', ['a3_19', 'a3_20']),
    ('(a3_03=1)', ['a3_04']),
    ('(g5_04a>=12)', ['g5_05']),  # Really for child modules
    ('(&(a4_01=1)(|(a4_02_2=1)(a4_02_3=1)(a4_02_4=1)(a4_02_5a=1)))', ['a4_03']),
]

SHORT_FORM_FREE_TEXT_CONVERSION = {
    'a_7_1': 'kidney',
    'a_7_2': 'dialysis',
    'a_7_3': 'fever',
    'a_7_4': 'ami',
    'a_7_5': 'heart',
    'a_7_6': 'jaundice',
    'a_7_7': 'liver',
    'a_7_8': 'malaria',
    'a_7_9': 'pneumonia',
    'a_7_10': 'renal',
    'a_7_11': 'suicide',
}

"""
Variables that contain free text.
"""
FREE_TEXT_VARS = [
    'a5_01_9b',
    'a6_08',
    'a6_11',
    'a6_12',
    'a6_13',
    'a6_14',
    'a6_15',
    'a7_01',
]

"""
Variables that contain duration data.
"""
DURATION_VARS = [
    'a2_01',
    'a2_03',
    'a2_08',
    'a2_15',
    'a2_22',
    'a2_24',
    'a2_26',
    'a2_28',
    'a2_33',
    'a2_37',
    'a2_41',
    'a2_48',
    'a2_54',
    'a2_58',
    'a2_62',
    'a2_65',
    'a2_68',
    'a2_70',
    'a2_73',
    'a2_76',
    'a2_79',
    'a2_83',
    'a2_86',
    'a3_08',
    'a3_11',
    'a3_16',
    'a5_04'
]

# TODO - Review this. 'a3_16' was in this list, but it causes a problem later in tariff.
DURATION_VARS_SHORT_FORM_DROP_LIST = [
]

"""
Duration variables that should contain a different value if a special case is detected.
"""
DURATION_VARS_SPECIAL_CASE = {
    'a5_04': 999
}