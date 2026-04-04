import json
import argparse


def _read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def data_parser(file_path1, file_path2):
    try:
        data1 = _read_json(file_path1)
        data2 = _read_json(file_path2)
        return data1, data2
    except FileNotFoundError:
        print('Invalid file path!')

def arg_parser():

    arg_parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    arg_parser.add_argument("first_file")
    arg_parser.add_argument("second_file")
    args = arg_parser.parse_args()
    
    return args.first_file, args.second_file
