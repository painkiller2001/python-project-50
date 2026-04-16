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
    
    return f'''
{{
{formatted_result}
}}
        '''
