import json

from gendiff.diff.formatters.json import format_json


def test_json_formatter_empty_diff():
    diff = []
    expected = "[]"
    assert format_json(diff) == expected


def test_json_formatter_simple_diff():
    diff = [
        {"key": "a", "type": "unchanged", "value": 1},
        {"key": "b", "type": "added", "value": 2}
    ]
    expected = json.dumps(diff, indent=2)
    assert format_json(diff) == expected


def test_json_formatter_nested():
    diff = [
        {
            "key": "nested",
            "type": "nested",
            "children": [
                {"key": "x", "type": "changed", "old_value": 1, "new_value": 2}
            ]
        }
    ]
    expected = json.dumps(diff, indent=2)
    assert format_json(diff) == expected