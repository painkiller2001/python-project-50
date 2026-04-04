import argparse
from gen_diff.cli import welcome_user
from .parser import data_parser


STORAGE_LINK = 'C:/Users/MSI/python-project-50/gen_diff/storage/'


def main():
    welcome_user()


def get_reference_information():
    ...


def arg_parser():

    arg_parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    arg_parser.add_argument("first_file")
    arg_parser.add_argument("second_file")
    args = arg_parser.parse_args()
    
    return args.first_file, args.second_file


def generate_diff():

    data_file1, data_file2 = arg_parser()


    default_path1 = f'{STORAGE_LINK}{data_file1}'
    default_path2 = f'{STORAGE_LINK}{data_file2}'

    parsed_data1, parsed_data2 = data_parser(default_path1, default_path2)

    result = {}

    sorted_data_file1 = dict(sorted(parsed_data1.items()))
    sorted_data_file2 = dict(sorted(parsed_data2.items()))

    for key, value in sorted_data_file1.items():
        if key not in sorted_data_file2:
            result[f'- {key}'] = str(value).lower()
        if key in sorted_data_file2 and sorted_data_file1[key] == sorted_data_file2[key]:
            result[f'  {key}'] = str(value).lower()
        if key in sorted_data_file2 and sorted_data_file1[key] != sorted_data_file2[key]:
            result[f'- {key}'] = str(value).lower()
            result[f'+ {key}'] = str(sorted_data_file2[key]).lower()

    for key, value in sorted_data_file2.items():
        if f'  {key}' in result:
            continue
        else:
            result[f'+ {key}'] = str(value).lower()
        
    formatted_result = '\n'.join(f"{key}: {value}" for key, value in result.items())

    print(f'''
{{
{formatted_result}
}}
        ''')
    
    return formatted_result
