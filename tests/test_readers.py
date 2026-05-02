from pathlib import Path

from gendiff.diff.support_funcs.readers import _read_json, _read_yaml

TEST_DATA_DIR = Path(__file__).parent / 'test_data'


def test_json_basic_reader():
    file_path = TEST_DATA_DIR / 'test_data_file1.json'
    data = _read_json(file_path)
    expected = {
        "follow": False,
        "host": "hexlet.io",
        "proxy": "123.234.53.22",
        "timeout": 50,
    }
    assert data == expected


def test_json_compl_reader():
    file_path = TEST_DATA_DIR / 'test_data_file5.json'
    data = _read_json(file_path)
    expected = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}
    assert data == expected


def test_yml_basic_reader():
    file_path = TEST_DATA_DIR / 'test_data_file4.yml'
    data = _read_yaml(file_path)
    expected = {
  "timeout": 40,
  "verbose": True,
  "host": "hexlet.io",
  "holdername": "Valery"
}
    assert data == expected


def test_yml_compl_reader():
    file_path = TEST_DATA_DIR / 'test_data_file6.yml'
    data = _read_yaml(file_path)
    expected = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}
    assert data == expected