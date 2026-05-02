from pathlib import Path

from gendiff.diff.gendiff import generate_diff
from tests.test_data.expected_results.result_formatters import (
    result_gendiff_json,
    result_gendiff_plain,
    result_gendiff_stylish,
)

get_expected_result_json = result_gendiff_json.get_expected_result_json
get_expected_result_plain = result_gendiff_plain.get_expected_result_plain
get_expected_result_stylish = result_gendiff_stylish.get_expected_result_stylish

TEST_DATA_DIR = Path(__file__).parent / 'test_data'

EXPECTED_STYLISH_BASIC = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_generate_diff_stylish_basic_json():
    result = generate_diff(
        'test_data_file1.json',
        'test_data_file2.json',
        'stylish',
        TEST_DATA_DIR
    )
    assert result.strip() == EXPECTED_STYLISH_BASIC.strip()


def test_generate_diff_stylish_basic_yaml():
    result = generate_diff(
        'test_data_file1.yml',
        'test_data_file2.yml',
        'stylish',
        TEST_DATA_DIR
    )
    assert result.strip() == EXPECTED_STYLISH_BASIC.strip()


def test_generate_diff_stylish_complex_json():
    expected = get_expected_result_stylish().strip()
    result = generate_diff(
        'test_data_file5.json',
        'test_data_file6.json',
        'stylish',
        TEST_DATA_DIR
    )
    assert result.strip() == expected


def test_generate_diff_stylish_complex_yaml():
    expected = get_expected_result_stylish().strip()
    result = generate_diff(
        'test_data_file5.yml',
        'test_data_file6.yml',
        'stylish',
        TEST_DATA_DIR
    )
    assert result.strip() == expected


def test_generate_diff_plain_complex_json():
    expected = get_expected_result_plain().strip()
    result = generate_diff(
        'test_data_file5.json',
        'test_data_file6.json',
        'plain',
        TEST_DATA_DIR
    )
    assert result.strip() == expected


def test_generate_diff_plain_complex_yaml():
    expected = get_expected_result_plain().strip()
    result = generate_diff(
        'test_data_file5.yml',
        'test_data_file6.yml',
        'plain',
        TEST_DATA_DIR
    )
    assert result.strip() == expected


def test_generate_diff_json_complex_json():
    result = generate_diff(
        'test_data_file5.json',
        'test_data_file6.json',
        'json',
        TEST_DATA_DIR
    )
    expected = get_expected_result_json()
    assert result.strip() == expected.strip()


def test_generate_diff_json_complex_yaml():
    expected = get_expected_result_json().strip()
    result = generate_diff(
        'test_data_file5.yml',
        'test_data_file6.yml',
        'json',
        TEST_DATA_DIR
    )
    assert result.strip() == expected