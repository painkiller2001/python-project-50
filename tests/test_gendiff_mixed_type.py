from pathlib import Path

from gen_diff.diff.gendiff import generate_diff

TEST_DATA_DIR = Path(__file__).parent / 'test_data'


def test_generate_diff_stylish_basic_json():

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


def test_generate_diff_stylish_basic_yaml():

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


def test_generate_diff_stylish_complicated_json():

    # tests of the correct sorted order of all elements

    file1 = 'test_data_file5.json'
    file2 = 'test_data_file6.json'
    
    result = generate_diff(file1, file2, TEST_DATA_DIR)
    
    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
'''

    assert result.strip() == expected.strip()


def test_generate_diff_stylish_complicated_yaml():

    # tests of the correct sorted order of all elements

    file1 = 'test_data_file5.yml'
    file2 = 'test_data_file6.yml'
    
    result = generate_diff(file1, file2, TEST_DATA_DIR)
    
    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
'''

    assert result.strip() == expected.strip()


def test_generate_diff_plain_format_json():

    # tests of the correct sorted order of all elements

    file5 = 'test_data_file5.json'
    file6 = 'test_data_file6.json'
    
    result = generate_diff(file5, file6, TEST_DATA_DIR, 'plain')
    
    expected = '''
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
'''

    assert result.strip() == expected.strip()


def test_generate_diff_plain_format_yaml():

    # tests of the correct sorted order of all elements

    file5 = 'test_data_file5.yml'
    file6 = 'test_data_file6.yml'
    
    result = generate_diff(file5, file6, TEST_DATA_DIR, 'plain')
    
    expected = '''
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
'''

    assert result.strip() == expected.strip()


def test_generate_diff_json_format_json():

    # tests of the correct sorted order of all elements

    file5 = 'test_data_file5.json'
    file6 = 'test_data_file6.json'
    
    result = generate_diff(file5, file6, TEST_DATA_DIR, 'json')
    
    expected = '''
[
  {
    "key": "common",
    "type": "nested",
    "children": [
      {
        "key": "follow",
        "type": "added",
        "value": false
      },
      {
        "key": "setting1",
        "type": "unchanged",
        "value": "Value 1"
      },
      {
        "key": "setting2",
        "type": "removed",
        "value": 200
      },
      {
        "key": "setting3",
        "type": "changed",
        "old_value": true,
        "new_value": null
      },
      {
        "key": "setting4",
        "type": "added",
        "value": "blah blah"
      },
      {
        "key": "setting5",
        "type": "added",
        "value": {
          "key5": "value5"
        }
      },
      {
        "key": "setting6",
        "type": "nested",
        "children": [
          {
            "key": "doge",
            "type": "nested",
            "children": [
              {
                "key": "wow",
                "type": "changed",
                "old_value": "",
                "new_value": "so much"
              }
            ]
          },
          {
            "key": "key",
            "type": "unchanged",
            "value": "value"
          },
          {
            "key": "ops",
            "type": "added",
            "value": "vops"
          }
        ]
      }
    ]
  },
  {
    "key": "group1",
    "type": "nested",
    "children": [
      {
        "key": "baz",
        "type": "changed",
        "old_value": "bas",
        "new_value": "bars"
      },
      {
        "key": "foo",
        "type": "unchanged",
        "value": "bar"
      },
      {
        "key": "nest",
        "type": "changed",
        "old_value": {
          "key": "value"
        },
        "new_value": "str"
      }
    ]
  },
  {
    "key": "group2",
    "type": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  {
    "key": "group3",
    "type": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
]
'''

    assert result.strip() == expected.strip()


def test_generate_diff_json_format_yaml():

    # tests of the correct sorted order of all elements

    file5 = 'test_data_file5.yml'
    file6 = 'test_data_file6.yml'
    
    result = generate_diff(file5, file6, TEST_DATA_DIR, 'json')
    
    expected = '''
[
  {
    "key": "common",
    "type": "nested",
    "children": [
      {
        "key": "follow",
        "type": "added",
        "value": false
      },
      {
        "key": "setting1",
        "type": "unchanged",
        "value": "Value 1"
      },
      {
        "key": "setting2",
        "type": "removed",
        "value": 200
      },
      {
        "key": "setting3",
        "type": "changed",
        "old_value": true,
        "new_value": null
      },
      {
        "key": "setting4",
        "type": "added",
        "value": "blah blah"
      },
      {
        "key": "setting5",
        "type": "added",
        "value": {
          "key5": "value5"
        }
      },
      {
        "key": "setting6",
        "type": "nested",
        "children": [
          {
            "key": "doge",
            "type": "nested",
            "children": [
              {
                "key": "wow",
                "type": "changed",
                "old_value": "",
                "new_value": "so much"
              }
            ]
          },
          {
            "key": "key",
            "type": "unchanged",
            "value": "value"
          },
          {
            "key": "ops",
            "type": "added",
            "value": "vops"
          }
        ]
      }
    ]
  },
  {
    "key": "group1",
    "type": "nested",
    "children": [
      {
        "key": "baz",
        "type": "changed",
        "old_value": "bas",
        "new_value": "bars"
      },
      {
        "key": "foo",
        "type": "unchanged",
        "value": "bar"
      },
      {
        "key": "nest",
        "type": "changed",
        "old_value": {
          "key": "value"
        },
        "new_value": "str"
      }
    ]
  },
  {
    "key": "group2",
    "type": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  {
    "key": "group3",
    "type": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
]
'''

    assert result.strip() == expected.strip()