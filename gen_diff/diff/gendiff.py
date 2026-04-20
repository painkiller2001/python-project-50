from pathlib import Path

from gen_diff.cli import welcome_user

from .parser import arg_parser, data_parser

STORAGE_LINK = Path(__file__).parent.parent / 'storage'


def main():
    welcome_user()


def get_reference_information():
    ...


def generate_diff(data_file1=None, data_file2=None, storage=None):

    if storage is None:
        storage = STORAGE_LINK

    if data_file1 is None or data_file2 is None:
        data_file1, data_file2 = arg_parser()  # file name parsing if args is empty

    default_path1 = Path(data_file1) if Path(data_file1).is_absolute() else storage / data_file1
    default_path2 = Path(data_file2) if Path(data_file2).is_absolute() else storage / data_file2

    parsed_data1, parsed_data2 = data_parser(str(default_path1), str(default_path2))

    diff = build_diff(parsed_data1, parsed_data2)

    result = format_stylish(diff)

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
        elif dict1[key] == dict2[key]:
            result.append({'key': key, 'type': 'unchanged', 'value': dict1[key]})
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                result.append({
                    'key': key,
                    'type': 'nested',
                    'children': build_diff(dict1[key], dict2[key])
                })
            else:
                result.append({
                    'key': key, 
                    'type': 'changed',
                    'old_value': dict1[key], 
                    'new_value': dict2[key]
                })
    
    return result


def format_stylish(diff, step=0):
    indent = '    ' * step
    lines = []
    
    for node in diff:
        if node['type'] == 'nested':
            lines.append(f"{indent}  {node['key']}: {{")
            lines.append(format_stylish(node['children'], step + 1))
            lines.append(f"{indent}  }}")
        
        elif node['type'] == 'changed':
            lines.append(f"{indent}- {node['key']}: {node['old_value']}")
            lines.append(f"{indent}+ {node['key']}: {node['new_value']}")
        
        elif node['type'] == 'added':
            lines.append(f"{indent}+ {node['key']}: {node['value']}")
        
        elif node['type'] == 'removed':
            lines.append(f"{indent}- {node['key']}: {node['value']}")
        
        elif node['type'] == 'unchanged':
            lines.append(f"{indent}  {node['key']}: {node['value']}")
    
    return '\n'.join(lines)