from gen_diff.cli import welcome_user


def main():
    welcome_user()

def get_reference_information():
    print('''
        usage: gendiff [-h] [-f FORMAT] first_file second_file

        Compares two configuration files and shows a difference.

        positional arguments:
        first_file
        second_file

        options::
        -h, --help            show this help message and exit
        -f FORMAT, --format FORMAT
                                set format of output
        ''')

def generate_diff(file1, file2):

    result = {}

    sorted_data_file1 = dict(sorted(file1.items()))
    sorted_data_file2 = dict(sorted(file2.items()))

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

    return formatted_result