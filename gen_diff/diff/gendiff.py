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