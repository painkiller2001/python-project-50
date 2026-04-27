from pathlib import Path

from .formatters.json import format_json
from .formatters.plain import get_format_plain_result
from .formatters.stylish import format_stylish
from .support_funcs.diff_builder import build_diff
from .support_funcs.parser import arg_parser, data_parser

STORAGE_LINK = Path(__file__).parent.parent / 'storage'


def generate_diff(
        data_file1=None, 
        data_file2=None, 
        storage=None, 
        format_name='stylish'
        ):

    if storage is None:
        storage = STORAGE_LINK

    if data_file1 is None or data_file2 is None:
        data_file1, data_file2, format_name = arg_parser()

    default_path1 = (Path(data_file1) 
        if Path(data_file1).is_absolute() 
        else storage / data_file1)
    
    default_path2 = (Path(data_file2) 
        if Path(data_file2).is_absolute() 
        else storage / data_file2)

    parsed_data1, parsed_data2 = data_parser(
        str(default_path1), 
        str(default_path2)
        )

    diff = build_diff(parsed_data1, parsed_data2)
    
    if format_name == 'stylish':
        result = format_stylish(diff)

    if format_name == 'plain':
        result = get_format_plain_result(diff)
        print(result)
        return result

    if format_name == 'json':
        result = format_json(diff)
        print(result)
        return result

    print(f"{{\n{result}\n}}")

    return f"{{\n{result}\n}}"