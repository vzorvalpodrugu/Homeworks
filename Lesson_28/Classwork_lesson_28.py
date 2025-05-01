"""Классная работа. Занятие 28"""
import json
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class TranscriptionChunk:
    text: str
    float_start: float
    float_stop: float
    str_start: str = field(init = False)
    str_stop: str = field(init = False)

    def __post_init__(self):
        self.str_start = self._float_to_str(self.float_start)
        self.str_stop = self._float_to_str(self.float_stop)

    def _float_to_str(self, float_time: float) -> str:
        """
        Преобразует float время в строковое
        :param float_time:
        :return:
        """
        seconds = int(float_time)
        minutes = seconds // 60
        seconds = seconds % 60
        hours = minutes // 60
        minutes = minutes % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

class TranscriptionIterator:
    def __init__(self, transcription_data: List[Dict[str: str, str: List[float]]]):
        self.transcription_data = transcription_data
        self.index = 0

    def __iter__(self):
        print("Сработал итератор")
        return self

    def __next__(self):
        if self.index >= len(self.transcription_data):
            raise StopIteration

        data = self.transcription_data[self.index]
        self.index += 1
        return self._serialazer(data)

    def _serialazer(self, data: Dict):
        text = data["text"]
        start = data["timestamp"][0]
        stop = data["timestamp"][1] if data["timestamp"][1] is not None else data["timestamp"][0]
        return TranscriptionChunk(text, start, stop)

def main():
    test_data = [
        {
        "timestamp": [0.0, 164.99],
        "text": "Привет, мир!"
        }
    ]

    with open("file.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    iterator = TranscriptionIterator(data)
    for chunk in iterator:
        print(chunk)

def transform_cities_data(input_file, output_file):
    # Read the original JSON data
    with open(input_file, 'r', encoding='utf-8') as file:
        cities = json.load(file)

    # Transform the data structure
    transformed_cities = []
    for city in cities:
        transformed_city = {
            "coords": {
                "lat": str(city["latitude"]),
                "lon": str(city["longitude"])
            },
            "district": city["district"],
            "name": city["name"],
            "population": city["population"],
            "subject": city["subject"]
        }
        transformed_cities.append(transformed_city)

    # Write the transformed data to a new file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(transformed_cities, file, ensure_ascii=False, indent=4)

    return transformed_cities


# Example usage
if __name__ == "__main__":
    transform_cities_data("../lesson_24/cities.json", "city.json")


# if __name__ == "__main__":
    # main()