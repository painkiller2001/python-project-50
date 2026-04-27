
def format_plain(diff, path=''):
    lines = []
    for node in diff:
        if isinstance(node, list):
            lines.extend(format_plain(node, path))
        else:
            current_key = node['key']
            full_path = f"{path}.{current_key}" if path else current_key

            if node['type'] == 'added':
                val = node['value']
                if isinstance(val, dict | list):
                    upd_value = '[complex value]'
                elif isinstance(val, bool) or val == 'null':
                    upd_value = str(val).lower()
                else:
                    upd_value = f"'{str(val)}'"
                lines.append(
                    f"Property '{full_path}' was added with value: {upd_value}"
                )

            if node['type'] == 'removed':
                lines.append(f"Property '{full_path}' was removed")

            if node['type'] == 'changed':
                old = node['old_value']
                if old is None:
                    upd_old = 'null'
                elif isinstance(old, (dict, list)):
                    upd_old = '[complex value]'
                elif isinstance(old, bool):
                    upd_old = str(old).lower()
                else:
                    upd_old = f"'{str(old)}'"

                new = node['new_value']
                if new is None:
                    upd_new = 'null'
                elif isinstance(new, (dict, list)):
                    upd_new = '[complex value]'
                elif isinstance(new, bool):
                    upd_new = str(new).lower()
                else:
                    upd_new = f"'{str(new)}'"

                lines.append(
                    f"Property '{full_path}' was updated. "
                    f"From {upd_old} to {upd_new}"
                )

            if 'children' in node and isinstance(node['children'], list):
                lines.extend(format_plain(node['children'], full_path))

    return lines


def get_format_plain_result(diff):
    return '\n'.join(format_plain(diff))