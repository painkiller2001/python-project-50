from gen_diff.cli import welcome_user
from .parser import data_parser, arg_parser


STORAGE_LINK = 'C:/Users/MSI/python-project-50/gen_diff/storage/'


def main():
    welcome_user()


def get_reference_information():
    ...

def generate_diff():

    data_file1, data_file2 = arg_parser()


    default_path1, default_path2 = f'{STORAGE_LINK}{data_file1}', f'{STORAGE_LINK}{data_file2}'

    parsed_data1, parsed_data2 = data_parser(default_path1, default_path2)

    result = {}

    common_unique_keys = sorted(tuple(set(list(parsed_data1.keys()) + list(parsed_data2.keys()))))

    for key in common_unique_keys:
        if key in parsed_data1 and key not in parsed_data2:
            result[f'- {key}'] = str(parsed_data1[key]).lower()
        if key in parsed_data2 and key not in parsed_data1:
            result[f'+ {key}'] = str(parsed_data2[key]).lower()
        if key in parsed_data2 and key in parsed_data1:
            if parsed_data1[key] == parsed_data2[key]:    
                result[f'  {key}'] = str(parsed_data2[key]).lower() 
            else:
                result[f'- {key}'] = str(parsed_data1[key]).lower()
                result[f'+ {key}'] = str(parsed_data2[key]).lower()
            
    formatted_result = '\n'.join(f"{key}: {value}" for key, value in result.items())

    print(f'''
{{
{formatted_result}
}}
        ''')
    
    return formatted_result
