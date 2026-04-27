from pathlib import Path

from gen_diff.diff.support_funcs.parser import data_parser

TEST_DATA_DIR = Path(__file__).parent / 'test_data'


def test_data_parser_two_jsons():
    file1 = TEST_DATA_DIR / 'test_data_file1.json'
    file2 = TEST_DATA_DIR / 'test_data_file2.json'
    
    data1, data2 = data_parser(file1, file2)
    
    expected1 = {
        "follow": False,
        "host": "hexlet.io",
        "proxy": "123.234.53.22",
        "timeout": 50,
    }
    expected2 = {
        "host": "hexlet.io",
        "timeout": 20,
        "verbose": True
    }
    
    assert data1 == expected1
    assert data2 == expected2


def test_data_parser_json_and_yaml():
    file1 = TEST_DATA_DIR / 'test_data_file1.json'
    file2 = TEST_DATA_DIR / 'test_data_file4.yml'
    
    data1, data2 = data_parser(file1, file2)
    
    expected1 = {
        "follow": False,
        "host": "hexlet.io",
        "proxy": "123.234.53.22",
        "timeout": 50,
    }
    expected2 = {
        "timeout": 40,
        "verbose": True,
        "host": "hexlet.io",
        "holdername": "Valery"
    }
    
    assert data1 == expected1
    assert data2 == expected2


def test_data_parser_missed_file():
    file1 = TEST_DATA_DIR / 'no_such_file.json'
    file2 = TEST_DATA_DIR / 'test_data_file2.json'
    
    data1, data2 = data_parser(file1, file2)
    
    assert data1 is None
    assert data2 is None


def test_data_parser_unsupported_extension():
    file1 = TEST_DATA_DIR / 'test_data_file1.json'
    file2 = TEST_DATA_DIR / 'test_data_file2.txt'
    
    data1, data2 = data_parser(file1, file2)
    
    assert data1 is None
    assert data2 is None