import json
import csv

json_string = """[
    "Монин Владимир Александрович",
    "Артемьев Алексей Львович",
    "Багатурян Ринат Дмитриевич",
    "Балагуров Артем Алексеевич",
    "Бибиков Кирилл Сергеевич",
    "Биков Илья Сергеевич",
    "Кражев Руслан Анатольевич",
    "Кузнецов Иван Станиславович",
    "Лямицкая Наталья Владимировна",
    "Мазуренко Кристина Владимировна",
    "Морозов Илья Валерьевич",
    "Мустац Иван Иванович",
    "Никулина Екатерина Александровна"
]"""

# python_data = json.loads(json_string)
# print(type(python_data))
# print(python_data)

# json_string = json.dumps(python_data, ensure_ascii=False)
# print(type(json_string))
# print(json_string)

# with open("students.json", 'w', encoding='utf-8') as file:
#     json.dump(python_data, file, ensure_ascii=False, indent=4)
#
# with open('students.json', 'r', encoding='utf-8') as file:
#         python_data = json.load(file)


def app_json(file_name: str, *data) -> None:
    """
    Appends data to a JSON file
    :param file_path:
    :param data:
    :return:
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        python_data = json.load(file)

        python_data.extend(data)

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(python_data, file, ensure_ascii=False, indent=4)

app_json('students.json', "Новый студент")
new_students = ["Студент сука1", "Студент сука2", "Студент сука3"]

app_json('students.json', *new_students)

students_list = [
    ["last_name", "first_name", "middle_name"],
    ["Монин", "Владимир", "Александрович"],
    ["Артемьев", "Алексей", "Львович"],
    ["Багатурян", "Ринат", "Дмитриевич"],
    ["Балагуров", "Артем", "Алексеевич"],
    ["Бибиков", "Кирилл", "Сергеевич"],
    ["Биков", "Илья", "Сергеевич"],
    ["Кражев", "Руслан", "Анатольевич"],
    ["Кузнецов", "Иван", "Станиславович"],
    ["Лямицкая", "Наталья", "Владимировна"],
    ["Мазуренко", "Кристина", "Владимировна"],
    ["Морозов", "Илья", "Валерьевич"],
    ["Мустац", "Иван", "Иванович"],
    ["Никулина", "Екатерина", "Александровна"]
]
# with open('students.csv', 'w', encoding='utf-8-sig') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\n')
#     writer.writerow(students_list)

#     writer - это объект csv.writer, через который мы пишем данные в CSV-файл
    # writer.writerow() - метод, который пишет одну строку в CSV-файл
    # в качестве аргумента он принимает список значений, которые нужно записать в эту строку

# with open('students.csv', 'r', encoding='utf-8-sig') as file:
#     reader = csv.reader(file, delimiter=';')
#     students_list = list(reader)
#
# students_new = ['Абрамкин', 'Леонид', 'по батюшке']
#
# students_list.append(students_new)

# чем отличается append от extend - append добавляет один элемент в конец списка, а extend добавляет список в конец списка

# with open('students.csv', 'a', encoding='utf-8-sig') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\n')
#     writer.writerows(new_students)
#
# print(students_list)


students_dict = [
    {"last_name": "Монин",
     "first_name": "Владимир",
     "middle_name": "Александрович"},

    {"last_name": "Артемьев",
     "first_name": "Алексей",
     "middle_name": "Львович"},

    {"last_name": "Багатурян",
     "first_name": "Ринат",
     "middle_name": "Дмитриевич"},

    {"last_name": "Балагуров",
     "first_name": "Артем", "middle_name": "Алексеевич"},
    {"last_name": "Бибиков", "first_name": "Кирилл",
     "middle_name": "Сергеевич"},

    {"last_name": "Биков",
     "first_name": "Илья",
     "middle_name": "Сергеевич"},

    {"last_name": "Кражев",
     "first_name": "Руслан",
     "middle_name": "Анатольевич"},

    {"last_name": "Кузнецов",
     "first_name": "Иван",
     "middle_name": "Станиславович"},

    {"last_name": "Лямицкая",
     "first_name": "Наталья",
     "middle_name": "Владимировна"},

    {"last_name": "Мазуренко",
     "first_name": "Кристина",
     "middle_name": "Владимировна"},

    {"last_name": "Морозов",
     "first_name": "Илья",
     "middle_name": "Валерьевич"},

    {"last_name": "Мустац",
     "first_name": "Иван",
     "middle_name": "Иванович"},

    {"last_name": "Никулина",
     "first_name": "Екатерина",
     "middle_name": "Александровна"}
]

# print((python_data))
# print(type(python_data))
