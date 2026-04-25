from pathlib import Path

from gen_diff.cli import welcome_user

from .parser import arg_parser, data_parser

STORAGE_LINK = Path(__file__).parent.parent / 'storage'


def main():
    welcome_user()


def get_reference_information():
    ...


def generate_diff(data_file1=None, data_file2=None, storage=None, format_name='stylish'):

    if storage is None:
        storage = STORAGE_LINK

    if data_file1 is None or data_file2 is None:
        data_file1, data_file2, format_name = arg_parser()  # file name parsing if args is empty

    default_path1 = Path(data_file1) if Path(data_file1).is_absolute() else storage / data_file1
    default_path2 = Path(data_file2) if Path(data_file2).is_absolute() else storage / data_file2

    parsed_data1, parsed_data2 = data_parser(str(default_path1), str(default_path2))

    diff = build_diff(parsed_data1, parsed_data2)
    
    if format_name == 'stylish':
        if '\'type\': \'nested\'' in str(diff):
            result = format_stylish_complicated(diff)
        else:
            result = format_stylish_basic(diff)

    if format_name == 'plain':
        result = get_format_plain_result(diff)
        print(result)
        return result

    if format_name == 'json':
        ...

    print(f"{{\n{result}\n}}")

    return f"{{\n{result}\n}}"


def build_diff(dict1, dict2):
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = []
    
    for key in all_keys:
        if key not in dict1:
            result.append({'key': key, 'type': 'added', 'value': dict2[key]})
        elif key not in dict2:
            result.append({'key': key, 'type': 'removed', 'value': dict1[key]})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(dict1[key], dict2[key])
            })
        elif dict1[key] == dict2[key]:
            result.append({'key': key, 'type': 'unchanged', 'value': dict1[key]})
        else:
            result.append({
                'key': key, 
                'type': 'changed',
                'old_value': dict1[key], 
                'new_value': dict2[key]
            })
    
    return result


def format_stylish_complicated(diff, step=0):
    indent = '    ' * step
    lines = []
    
    for node in diff:
        if node['type'] == 'nested':
            lines.append(f"{indent}    {to_str(node['key'])}: {{")
            lines.append(format_stylish_complicated(node['children'], step + 1))
            lines.append(f"{indent}    }}")
        
        elif node['type'] == 'changed':
            old_val = format_value(node['old_value'], step + 1)
            new_val = format_value(node['new_value'], step + 1)
            lines.append(f"{indent}  - {to_str(node['key'])}: {old_val}")
            lines.append(f"{indent}  + {to_str(node['key'])}: {new_val}")
        
        elif node['type'] == 'added':
            val = format_value(node['value'], step + 1)
            lines.append(f"{indent}  + {to_str(node['key'])}: {val}")
        
        elif node['type'] == 'removed':
            val = format_value(node['value'], step + 1)
            if val == '':
                lines.append(f"{indent}  - {to_str(node['key'])}:")
            else:
                lines.append(f"{indent}  - {to_str(node['key'])}: {val}")

        elif node['type'] == 'unchanged':
            val = format_value(node['value'], step + 1)
            lines.append(f"{indent}    {to_str(node['key'])}: {val}")
    
    return '\n'.join(lines)


def format_stylish_basic(diff):
    lines = []
    
    for node in diff:
       
        if node['type'] == 'changed':
            lines.append(f"  - {str(node['key'])}: {str(node['old_value']).lower()}")
            lines.append(f"  + {str(node['key'])}: {str(node['new_value']).lower()}")
        
        elif node['type'] == 'added':
            lines.append(f"  + {str(node['key'])}: {str(node['value']).lower()}")
        
        elif node['type'] == 'removed':
            lines.append(f"  - {str(node['key'])}: {str(node['value']).lower()}")

        elif node['type'] == 'unchanged':
            lines.append(f"    {str(node['key'])}: {str(node['value']).lower()}")
    
    return '\n'.join(lines)


def to_str(arg):
    if isinstance(arg, bool):
        return str(arg).lower()
    elif arg is None:
        return 'null'
    elif arg == '':
        return ''
    else:
        return arg
    

def str_dict(elem_dict, step):
    indent = '    ' * step
    lines = []
    for key, value in elem_dict.items():
        if isinstance(value, dict):
            lines.append(f"{indent}    {key}: {str_dict(value, step + 1)}")
        else:
            lines.append(f"{indent}    {key}: {to_str(value)}")
    return '{\n' + '\n'.join(lines) + f'\n{indent}}}'


def format_value(value, step):
    if isinstance(value, dict):
        return str_dict(value, step)
    else:
        return to_str(value)
    

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