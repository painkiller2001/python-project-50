

def format_stylish(diff, step=0):
    indent = '    ' * step
    lines = []
    
    for node in diff:
        if node['type'] == 'nested':
            lines.append(f"{indent}    {to_str(node['key'])}: {{")
            lines.append(format_stylish(node['children'], step + 1))
            lines.append(f"{indent}    }}")
        
        elif node['type'] == 'changed':
            old_val = format_value(node['old_value'], step + 1)
            new_val = format_value(node['new_value'], step + 1)
            if old_val == '':
                lines.append(f"{indent}  - {node['key']}: ")
            else:
                lines.append(f"{indent}  - {to_str(node['key'])}: {old_val}")
            if new_val == '':
                lines.append(f"{indent}  + {node['key']}:")
            else:
                lines.append(f"{indent}  + {to_str(node['key'])}: {new_val}")
        
        elif node['type'] == 'added':
            val = format_value(node['value'], step + 1)
            lines.append(f"{indent}  + {to_str(node['key'])}: {val}")
        
        elif node['type'] == 'removed':
            val = format_value(node['value'], step + 1)
            if val == '':
                lines.append(f"{indent}  - {to_str(node['key'])}: ")
            else:
                lines.append(f"{indent}  - {to_str(node['key'])}: {val}")

        elif node['type'] == 'unchanged':
            val = format_value(node['value'], step + 1)
            lines.append(f"{indent}    {to_str(node['key'])}: {val}")
    
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