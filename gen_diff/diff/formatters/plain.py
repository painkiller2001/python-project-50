

def format_plain(diff, path=''):
    lines = []
    for node in diff:
        if isinstance(node, list):
            lines.extend(format_plain(node, path))
        else:
            current_key = node['key']
            full_path = f"{path}.{current_key}" if path else current_key

            if node['type'] == 'added':
                upd_value = (
                    '[complex value]' if isinstance(node['value'], dict | list)
                    else str(node['value']).lower() if isinstance(node['value'], bool) or node['value'] == 'null'
                    else f"'{str(node['value'])}'")
                lines.append(f'Property \'{full_path}\' was added with value: {upd_value}')
            
            if node['type'] == 'removed':
                lines.append(f'Property \'{full_path}\' was removed')

            if node['type'] == 'changed':
                upd_old_value = ('null' if node['old_value'] is None
                    else '[complex value]' if isinstance(node['old_value'], (dict, list))
                    else str(node['old_value']).lower() if isinstance(node['old_value'], bool)
                    else f"'{str(node['old_value'])}'"
                    )
                upd_new_value = ('null' if node['new_value'] is None
                    else '[complex value]' if isinstance(node['new_value'], (dict, list))
                    else str(node['new_value']).lower() if isinstance(node['new_value'], bool)
                    else f"'{str(node['new_value'])}'"
                    )

                lines.append(f'Property \'{full_path}\' was updated. From {upd_old_value} to {upd_new_value}')

            if 'children' in node and isinstance(node['children'], list):
                lines.extend(format_plain(node['children'], full_path))

    return lines


def get_format_plain_result(diff):
    return '\n'.join(format_plain(diff))