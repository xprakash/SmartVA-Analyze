# new headers generated by this step in processing
GENERATED_HEADERS_DATA = [
    ('g4_03b', 0),
    ('a2_01b', 0),
    ('a2_22b', 0),
    ('a2_24b', 0),
    ('a2_26b', 0),
    ('a2_28b', 0),
    ('a2_33b', 0),
    ('a2_37b', 0),
    ('a2_41b', 0),
    ('a2_54b', 0),
    ('a2_58b', 0),
    ('a2_62b', 0),
    ('a2_65b', 0),
    ('a2_68b', 0),
    ('a2_70b', 0),
    ('a2_73b', 0),
    ('a2_76b', 0),
    ('a2_79b', 0),
    ('a2_83b', 0),
    ('a2_86b', 0),
    ('a4_02_1', 0),
    ('a4_02_2', 0),
    ('a4_02_3', 0),
    ('a4_02_4', 0),
    ('a4_02_5a', 0),
    ('a4_02_6', 0),
    ('a4_02_7', 0),
    ('a5_01_8', 0),
    ('a5_04b', ''),
    ('a6_02_1', 0),
    ('a6_02_2', 0),
    ('a6_02_3', 0),
    ('a6_02_4', 0),
    ('a6_02_5', 0),
    ('a6_02_6', 0),
    ('a6_02_8', 0),
    ('a6_02_9', 0),
    ('a6_02_10', 0),
    ('a6_02_11', 0),
    ('a6_02_12a', 0),
    ('a6_02_13', 0),
    ('a6_02_14', 0),
    ('a6_02_15', 0),
]

"""
Consolidation maps use the format:
    (read_header, write_header): {
        VAL: data_header
    }
"""
CONSOLIDATION_MAP = {
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

FREE_TEXT_HEADERS = [
    'a5_01_9b',
    'a6_08',
    'a6_11',
    'a6_12',
    'a6_13',
    'a6_14',
    'a6_15',
    'a7_01',
]
