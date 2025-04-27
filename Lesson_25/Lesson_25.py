from idlelib.configdialog import is_int

from marvel import full_dict

# Получаем ввод от пользователя, где цифры вводятся через пробел
user_input = input("Введите цифры через пробел: ")

# Разбиваем введённую строку на список с помощью метода split()
numbers_list = user_input.split()
# print(numbers_list)

# Здесь конечно в иишку подсмотрел, а то минут 30 варианты накидывал и не получалось, но сейчас разобрался жестко и всё понял
withNoneList = list(map(lambda num: int(num) if (num.isdigit() or (num[0] == '-' and num[1:].isdigit()))  else None, numbers_list))
# print(withNoneList)

# Фильтруем список с помощью функции filter()

filtered_list = dict(filter(lambda item: item[0] in withNoneList, full_dict.items()))
# print(filtered_list)

# пункт 4
set_filtered_list = {value["director"] for key, value in full_dict.items()}
# print(set_filtered_list)

# # пункт 5
copy_full_dict = {key: {**value, 'year': str(value['year'])} for key, value in full_dict.items()}
# print(copy_full_dict)

# пункт 6
filtered_movies = dict(filter(lambda item: item[1]['title'] is not None and item[1]['title'][0].lower() == 'ч', full_dict.items()))
# print(filtered_movies)

# пункт 7 У вас была ошибка на занятии, потому что в одном из фильмов, название было None
sort_movies = sorted(full_dict.items(), key=lambda item: item[1]['title'] is not None)
# print(sort_movies)

# пункт 8
sort_movies_ = sorted(full_dict.items(), key=lambda item: (item[1]['title'] is not None, item[1]['year'] is int))
# print(sort_movies)

# пункт 9
filt_sort_movies = sorted(dict(filter(lambda item: item[0]<20,full_dict.items())).items(), key=lambda item: item[1]['year'])
# print(filt_sort_movies)

from pprint import pprint
print("Задание 2")
pprint(withNoneList, sort_dicts=False)

print("Задание 3")
pprint(filtered_list, sort_dicts=False)

print("Задание 4")
pprint(set_filtered_list, sort_dicts=False)

print("Задание 5")
pprint(copy_full_dict, sort_dicts=False)

print("Задание 6")
pprint(filtered_movies, sort_dicts=False)

print("Задание 7")
pprint(sort_movies, sort_dicts=False)

print("Задание 8")
pprint(sort_movies_, sort_dicts=False)

print("Задание 9")
pprint(filt_sort_movies, sort_dicts=False)