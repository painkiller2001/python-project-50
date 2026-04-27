from gen_diff.diff.formatters.stylish import format_stylish


def test_stylish_unchanged():
    diff = [{"key": "a", "type": "unchanged", "value": 1}]
    expected = "    a: 1"
    assert format_stylish(diff) == expected


def test_stylish_added():
    diff = [{"key": "b", "type": "added", "value": 2}]
    expected = "  + b: 2"
    assert format_stylish(diff) == expected


def test_stylish_removed():
    diff = [{"key": "c", "type": "removed", "value": 3}]
    expected = "  - c: 3"
    assert format_stylish(diff) == expected


def test_stylish_changed():
    diff = [{"key": "d", "type": "changed", "old_value": 4, "new_value": 5}]
    expected = "  - d: 4\n  + d: 5"
    assert format_stylish(diff) == expected


def test_stylish_nested():
    diff = [
        {
            "key": "e",
            "type": "nested",
            "children": [
                {"key": "f", "type": "unchanged", "value": 6}
            ]
        }
    ]
    expected = "    e: {\n        f: 6\n    }"
    assert format_stylish(diff).strip() == expected.strip()