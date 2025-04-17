import json
import random
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
# print(Serial.cities[1].name)

# print(file.read_data())

class CityGame:
    def __init__(self, cities: CitiesSerializer):
        self.cities = cities
        self.is_over = True
        self.human_city = ''
        self.computer_word = ''

    def start_game(self):
        self.is_over = False
        self.cities.load_cities()

    def human_turn(self):
        city_input = input()
        if city_input in self.cities.cities and self.computer_word[len(self.computer_word) - 1 ] == city_input[0]:
            self.cities.cities.is_used = True
            self.human_city = city_input
            print('Человечишка назвал город: ' + city_input)
        else:
            self.human_turn()

    def computer_turn(self):
        is_first = True
        rnd = random.randint(0, len(self.cities.cities) - 1)
        if is_first:
            computer_word = self.cities.cities[rnd].name
            is_first = False
            self.cities.cities[rnd].is_used = True
            print("Кампукта назвал город:" + computer_word)
        else:
            for city in self.cities.cities:
                if city[0] == self.human_city[len(self.human_city) - 1]:
                    computer_word = city
                    city.is_used = True
                    print("Кампукта назвал город:" + computer_word)
        pass

    def check_game_over(self):
        if self.human_city == self.computer_word:
            self.is_over = True
            print('Человечишка победил')
        elif self.computer_word == self.human_city:
            self.is_over = True
            print('Кампукта победил')
        pass

class GameManager:
    def __init__(self):
        self.game = CityGame(CitiesSerializer(JsonFile('json_file')))

    def run_game(self):
        return self.game.check_game_over()

    def __call__(self):
        self.game.start_game()
        while not self.game.is_over:
            self.game.human_turn()
            self.game.computer_turn()
            self.run_game()

if __name__ == "__main__":
    GameManager()


