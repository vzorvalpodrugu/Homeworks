import json
class JsonFile:
    """
    Класс для работы с json файлами
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        """
        Метод для чтения данных из json файла
        return data
        """
        with open(self.file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def write_data(self, data):
        """
        Метод для записи данных в json файл
        return None
        """
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

# file = JsonFile('cities.json')
# print(file.read_data())

