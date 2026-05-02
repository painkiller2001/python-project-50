
COMPLEX_VALUE = '[complex value]'


def _to_plain_value(value):
    if isinstance(value, dict):
        return COMPLEX_VALUE
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, (int, float)):
        return str(value)
    return f"'{value}'"


def _format_added(full_path, value):
    return (
        f"Property '{full_path}' was added with value: "
        f"{_to_plain_value(value)}"
    )


def _format_changed(full_path, old, new):
    old_val = _to_plain_value(old)
    new_val = _to_plain_value(new)
    return (
        f"Property '{full_path}' was updated. "
        f"From {old_val} to {new_val}"
    )


def _format_removed(full_path):
    return f"Property '{full_path}' was removed"


def _process_node(node, path):
    full_path = f"{path}.{node['key']}" if path else node['key']
    node_type = node['type']

    if node_type == 'added':
        return _format_added(full_path, node['value'])
    if node_type == 'removed':
        return _format_removed(full_path)
    if node_type == 'changed':
        return _format_changed(full_path, node['old_value'], node['new_value'])
    if node_type == 'nested':
        return format_plain(node['children'], full_path)
    return None


def format_plain(diff, path=''):
    lines = []
    for node in diff:
        result = _process_node(node, path)
        if result is None:
            continue
        if isinstance(result, list):
            lines.extend(result)
        else:
            lines.append(result)
    return lines


def get_format_plain_result(diff):
    return '\n'.join(format_plain(diff))