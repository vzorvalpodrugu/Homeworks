import json
from dataclasses import dataclass, field
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



@dataclass
class City:
    """
    Класс для хранения данных о городах
    """
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = field(default=False)

class CitiesSerializer:
    """
    Использует датакласс City для хранения информации о городах.
    """
    def __init__(self, json_file: JsonFile):
        self.json_file = json_file
        self.cities = []

    def load_cities(self):
        """
        Загружает данные о городах из json файла и создает объекты City.
        Returns:

        """
        cities_data = self.json_file.read_data()
        for city_data in cities_data:
            city = City(
                name=city_data['name'],
                population=city_data['population'],
                subject=city_data['subject'],
                district=city_data['district'],
                latitude=city_data['latitude'],
                longitude=city_data['longitude']
            )
            self.cities.append(city)

# file = JsonFile('cities.json')
# Serial = CitiesSerializer(file)
# Serial.load_cities()
# print(Serial.cities)

# print(file.read_data())

