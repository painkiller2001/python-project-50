from pathlib import Path

from gen_diff.diff.gendiff import generate_diff

TEST_DATA_DIR = Path(__file__).parent / 'test_data'


def test_generate_diff_basic_json():

    # tests of the correct sorted order of all elements

    file1 = 'test_data_file1.json'
    file2 = 'test_data_file2.json'
    
    result = generate_diff(file1, file2, TEST_DATA_DIR)
    
    expected = '''{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}
'''
        
    assert result.strip() == expected.strip()


def test_generate_diff_correct_result_type_json():

    # tests of the correctness of result type (str)

    file1 = 'test_data_file1.json'
    file2 = 'test_data_file2.json'
    
    result = generate_diff(file1, file2, TEST_DATA_DIR)
    
    assert isinstance(result, str)


def test_generate_diff_other_els_or_el_is_absent_json():

    # test if no element 'follow' in file2 and different name of element 'timeout'

    file1 = 'test_data_file1.json'
    file2 = 'test_data_file2.json'
    
    result = generate_diff(file1, file2, TEST_DATA_DIR)
        
    assert '- timeout: 50' in result
    assert '+ timeout: 20' in result
    assert '- follow: false' in result


def test_generate_diff_basic_yaml():

    # tests of the correct sorted order of all elements

    file1 = 'test_data_file1.yml'
    file2 = 'test_data_file2.yml'
    
    result = generate_diff(file1, file2, TEST_DATA_DIR)
    
    expected = '''{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}
'''
        
    assert result.strip() == expected.strip()


def test_generate_diff_correct_result_type_yaml():

    # tests of the correctness of result type (str)

    file1 = 'test_data_file1.yml'
    file2 = 'test_data_file2.yml'
    
    result = generate_diff(file1, file2, TEST_DATA_DIR)
    
    assert isinstance(result, str)


def test_generate_diff_other_els_or_el_is_absent_yaml():

    # test if no element 'follow' in file2 and different name of element 'timeout'

    file1 = 'test_data_file1.yml'
    file2 = 'test_data_file2.yml'
    
    result = generate_diff(file1, file2, TEST_DATA_DIR)
        
    assert '- timeout: 50' in result
    assert '+ timeout: 20' in result
    assert '- follow: false' in result