import json


def parser():
    file_path = input("Please, input path to JSON file: ")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(data)
    except FileNotFoundError:
        print('Invalid file path!')
