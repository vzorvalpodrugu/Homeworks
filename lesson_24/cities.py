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
        print("Города инициализированы")



# file = JsonFile('cities.json')
# Serial = CitiesSerializer(file)
# Serial.load_cities()
# print(Serial.cities[1].name)

# print(file.read_data())

class CityGame:
    """
    Класс для управления игрой в города
    """
    def __init__(self, cities: CitiesSerializer):
        """
        Инициализирует игру с заданными городами.
        Args:
            cities:
        """
        self.cities = cities
        self.is_over = True
        self.human_city: str = ''
        self.computer_word: str = ''
        self.is_first_turn = True

    def start_game(self):
        """
        Начинает игру.
        Returns:

        """
        self.is_over = False
        self.cities.load_cities()
        print("Игра началась!")
        self.computer_turn()

    def human_turn(self):
        """
        Выполняет ход игрока.
        Returns:

        """
        print("Компьютер назвал город: " + self.computer_word + ".\nТеперь ваша очередь)")
        self.human_city = input()
        if (any(city.name.lower() == self.human_city.lower() for city in self.cities.cities)) and self.computer_word[len(self.computer_word) - 1 ].lower() == self.human_city[0].lower():
            print('Человечишка назвал город: ' + self.human_city)
        elif any(city.name.lower() == self.human_city.lower() for city in self.cities.cities):
            print("Город есть в списке, но не подходит\nВы проиграли!")
        elif self.human_city[0].lower() == self.computer_word[len(self.computer_word)-1].lower():
            print("Буквы совпали, но города нет в списке\nВы проиграли!")
            self.is_over = True
        else:
            print("Вы проиграли!")
            self.is_over = True

        # print(self.computer_word, self.human_city)

    def computer_turn(self):
        """
        Выполняет ход компьютера.
        Returns:

        """
        if self.is_first_turn:
            rnd = random.randint(0, len(self.cities.cities) - 1)
            self.computer_word = self.cities.cities[rnd].name
            self.cities.cities[rnd].is_used = True
            print("Кампукта назвал город:" + self.computer_word)
            self.is_first_turn = False
        else:
            print("Человек назвал город: " + self.human_city + ".\nТеперь очередь компьютера! \n")
            for city in self.cities.cities:
                if city.name[0].lower() == self.human_city[len(self.human_city) - 1].lower():
                    self.computer_word = city.name
                    # self.cities.cities.city.is_used = True
                    # print(self.cities.cities)
                    city.is_used = True
                    print("Кампукта назвал город: " + self.computer_word)
                    break
            else:
                print("Компьютер проиграл!")
                self.is_over = True
        # print(self.computer_word, self.human_city)



class GameManager:
    """
    Класс для управления игрой
    """
    def __init__(self):
        self.game = CityGame(CitiesSerializer(JsonFile('cities.json')))

    # def run_game(self):
    #     return self.game.check_game_over()

    def __call__(self):
        self.game.start_game()
        while not self.game.is_over:
            self.game.human_turn()
            # self.run_game()
            if self.game.is_over:
                break
            self.game.computer_turn()


if __name__ == "__main__":
    game = GameManager()
    game()




