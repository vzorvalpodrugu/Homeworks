import json

def read_json(file_path: str, encoding: str = 'utf-8'):
    """
    Read data from a JSON file.
    Args:
        file_path (str): The file path to the JSON data.
        encoding (str, optional): The encoding of the JSON data. Defaults to 'utf-8'.
    Returns: dict: The parsed JSON data.
    """

    with open(file_path, 'r', encoding=encoding) as file:
        reader = json.load(file)


def write_json(file_path: str, *data, encoding: str = 'utf-8') -> None:
    """
    def: write data to a JSON file
    :param file_path: The file path to the JSON data.
    :param data: The data to be written as JSON.
    :param encoding: The encoding of the JSON data. Defaults to 'utf-8'.
    :return: None
    """

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(*data, file, ensure_ascii=False, indent=4)
# write_json('file.json', {'name': 'John Doe', 'age': 30, 'city': 'New York'})

def app_json(file_path: str, *data, encoding: str = 'utf-8', indent = 4) -> None:
    """
    def: additional write data to a JSON file
    :param file_path: The file path to the JSON data.
    :param data: The data to be written as JSON.
    :param encoding: The encoding of the JSON data. Defaults to 'utf-8'.
    :param indent: The number of spaces to indent each level of nesting. Defaults to 4.
    :return: None
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        python_data = json.load(file)

    python_data.extend(data)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(python_data, file, ensure_ascii=False, indent=indent)


import csv
def read_csv(file_path, encoding='windows-1251', delimiter=';'):
    """
    def: read data from a CSV file
    :param file_path: The file path to the CSV data.
    :param encoding: The encoding of the CSV data. Defaults to 'windows-1251'.
    :param delimiter: The delimiter used in the CSV file. Defaults to ';'.
    :return: list: The parsed CSV data.
    """
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter, lineterminator='\n')

def write_csv(file_path, data, encoding='windows-1251', delimiter=';'):
    """
    def: write data to a CSV file
    :param file_path: The file path to the CSV data.
    :param data: The data to be written as CSV.
    :param encoding: The encoding of the CSV data. Defaults to 'windows-1251'.
    :param delimiter: The delimiter used in the CSV file. Defaults to ';'.
    :return: None
    """
    with open(file_path, 'w', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator='\n')
        writer.writerows(data)

def append_csv(file_path, data, encoding='windows-1251', delimiter=';'):
    """
    def: append data to a CSV file
    :param file_path: The file path to the CSV data.
    :param data: The data to be appended as CSV.
    :param encoding: The encoding of the CSV data. Defaults to 'windows-1251'.
    :param delimiter: The delimiter used in the CSV file. Defaults to ';'.
    :return: None
    """
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter, lineterminator='\n')
        python_data = list(reader)

        python_data.extend(data)
    with open(file_path, 'w', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator='\n')
        writer.writerows(python_data)

def read_txt(file_path, encoding='utf-8'):
    """
    def: read data from a TXT file
    :param file_path: The file path to the TXT data.
    :param encoding: The encoding of the TXT data. Defaults to 'utf-8'.
    :return: str: The parsed TXT data.
    """
    with open(file_path, 'r', encoding=encoding) as file:
        output = file.read()
        return output


def write_txt(file_path, data, encoding='utf-8'):
    """
    def: write data to a TXT file
    :param file_path: The file path to the TXT data.
    :param data: The data to be written as TXT.
    :param encoding: The encoding of the TXT data. Defaults to 'utf-8'.
    :return None
    """
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(data)

def append_txt(file_path, data, encoding='utf-8'):
    """
    def: append data to a TXT file
    :param file_path: The file path to the TXT data.
    :param data: The data to be appended as TXT.
    :param encoding: The encoding of the TXT data. Defaults to 'utf-8'.
    :return None
    """
    with open(file_path, 'a', encoding=encoding) as file:
        file.write(data)

import yaml
def read_yaml(file_path):
    """
    def: read data from a YAML file
    :param file_path: The file path to the YAML data.
    :return: dict: The parsed YAML data.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        print(data)
        return data

read_yaml('weather.yaml')