import json
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class City:
    """
    City class representing a city with various attributes.
    """
    name: str
    lat: float
    lon: float
    district: str
    population: int
    subject: str

class ImportJsonData:
    """
    Class for importing and processing JSON data.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        """
        Read and return the JSON data from the file.
        Returns: JSON data as a dictionary.
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            print("File has been loaded")
            return json.load(file)


class CitiesIterator:
    """
    Iterator class for iterating over cities data.
    """
    def __init__(self, cities_data: List[Dict[str, str|int|Dict[str, str]]]):
        self.cities_data = cities_data
        self.min_population = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cities_data):
             raise StopIteration

        data = self.cities_data[self.index]
        self.index += 1
        return self.serialazer(data)

    def sort_by(self, parameter: str, reverse: bool = True):
        """
        Sort the cities data based on the specified parameter.
        :param parameter: The parameter to sort by (e.g., 'lat', 'lon', 'population').
        :param reverse: If True, sort in descending order; otherwise, sort in ascending order.
        :return: The sorted CitiesIterator object.
        """
        if not self.cities_data:
            return self

        if parameter in ['lat', 'lon']:
            self.cities_data.sort(
                key=lambda city: float(city['coords'][parameter]),
                reverse=reverse
            )

        elif parameter in self.cities_data[0]:
            self.cities_data.sort(
                key=lambda city: city[parameter],
                reverse=reverse
            )
        else:
            raise ValueError(f"Параметр '{parameter}' не найден в данных о городах")

        self.index = 0
        return self

    def set_population_filter(self, min_population: int):
        """
        Set the minimum population filter for the cities.
        Args:
            min_population: The minimum population value.
        Returns: None
        """
        self.min_population = min_population

    def serialazer(self, data: Dict):
        """
        Serialize the data into a City object.
        Args: data: The data to be serialized.
        Returns: A City object representing the serialized data.
        """
        for key, value in data.items():
            if value is None or value == "" or value == 0:
                raise ValueError(f"{key} is None")

        name = data['name']
        lat = data['coords']['lat']
        lot = data['coords']['lon']
        district = data['district']
        population = data['population']
        subject = data['subject']

        if population >= self.min_population:
            return City(name, lat, lot, district, population, subject)
        else:
            return None


def main():
    """
    Main function to execute the program.
    """
    import_data = ImportJsonData('city.json').read()
    iterator = CitiesIterator(import_data)

    iterator.set_population_filter(500000)
    iterator.sort_by('lat')

    for city in iterator:
        if city is not None:
            print(city)

if __name__ == '__main__':
    main()