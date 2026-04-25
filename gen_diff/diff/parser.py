import argparse
import json
from pathlib import Path

import yaml


def _read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
    
def _read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


FORMAT_FUNC = {'.json': _read_json,
               '.yml': _read_yaml,
               '.yaml': _read_yaml
                }


def data_parser(file_path1, file_path2):
    result = []
    try:
        for arg in [file_path1, file_path2]:
            result.append(FORMAT_FUNC[Path(arg).suffix](arg))                
        data1, data2 = result
        return data1, data2
    except FileNotFoundError:
        print('Invalid file path!')
        return None, None
    except KeyError:
        print('Unsupported file format! Use .json, .yml or .yaml')
        return None, None


def arg_parser():

    arg_parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    arg_parser.add_argument("first_file")
    arg_parser.add_argument("second_file")
    arg_parser.add_argument("--format", default='stylish', help='output format: stylish, plain, json')
    args = arg_parser.parse_args()
    
    return args.first_file, args.second_file, args.format