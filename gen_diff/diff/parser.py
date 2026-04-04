import json


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

