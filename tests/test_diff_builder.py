from gendiff.diff.support_funcs.diff_builder import build_diff


def test_empty():
    assert build_diff({}, {}) == []


def test_unchanged():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"a": 1, "b": 2}
    expected = [
        {"key": "a", "type": "unchanged", "value": 1},
        {"key": "b", "type": "unchanged", "value": 2},
    ]
    assert build_diff(dict1, dict2) == expected


def test_added():
    dict1 = {"a": 1}
    dict2 = {"a": 1, "b": 2}
    expected = [
        {"key": "a", "type": "unchanged", "value": 1},
        {"key": "b", "type": "added", "value": 2},
    ]
    assert build_diff(dict1, dict2) == expected


def test_removed():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"a": 1}
    expected = [
        {"key": "a", "type": "unchanged", "value": 1},
        {"key": "b", "type": "removed", "value": 2},
    ]
    assert build_diff(dict1, dict2) == expected


def test_changed():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"a": 1, "b": 3}
    expected = [
        {"key": "a", "type": "unchanged", "value": 1},
        {"key": "b", "type": "changed", "old_value": 2, "new_value": 3},
    ]
    assert build_diff(dict1, dict2) == expected


def test_nested():
    dict1 = {"a": {"b": 1}}
    dict2 = {"a": {"b": 2}}
    expected = [
        {
            "key": "a",
            "type": "nested",
            "children": [
                {"key": "b", "type": "changed", "old_value": 1, "new_value": 2}
            ]
        }
    ]
    assert build_diff(dict1, dict2) == expected


def test_all_types():
    dict1 = {
        "unchanged": 1,
        "removed": 2,
        "changed": 3,
        "nested": {"x": 10}
    }
    dict2 = {
        "unchanged": 1,
        "added": 4,
        "changed": 99,
        "nested": {"x": 20}
    }
    expected = [
        {"key": "added", "type": "added", "value": 4},
        {"key": "changed", "type": "changed", "old_value": 3, "new_value": 99},
        {"key": "nested", "type": "nested", "children": [
            {"key": "x", "type": "changed", "old_value": 10, "new_value": 20}
        ]},
        {"key": "removed", "type": "removed", "value": 2},
        {"key": "unchanged", "type": "unchanged", "value": 1},
    ]
    assert build_diff(dict1, dict2) == expected