from gendiff.diff.formatters.plain import get_format_plain_result


def test_plain_added():
    diff = [{"key": "b", "type": "added", "value": 2}]
    assert get_format_plain_result(diff) == (
        "Property 'b' was added with value: 2"
    )


def test_plain_removed():
    diff = [{"key": "b", "type": "removed", "value": 2}]
    assert get_format_plain_result(diff) == "Property 'b' was removed"


def test_plain_changed():
    diff = [
        {"key": "b", "type": "changed", "old_value": None, "new_value": False}
    ]
    assert get_format_plain_result(diff) == (
        "Property 'b' was updated. From null to false"
    )


def test_plain_nested():
    diff = [
        {
            "key": "a",
            "type": "nested",
            "children": [
                {"key": "b", "type": "added", "value": "cat"}
            ]
        }
    ]
    expected = "Property 'a.b' was added with value: 'cat'"
    assert get_format_plain_result(diff) == expected


def test_plain_complex_value():
    diff = [{"key": "c", "type": "added", "value": {"x": "hello"}}]
    assert get_format_plain_result(diff) == (
        "Property 'c' was added with value: [complex value]"
    )