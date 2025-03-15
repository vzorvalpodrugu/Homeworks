# # Задача 1: Анализ чисел
# # Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# # и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
# #
# numbers = [1, 2, 3, 4, 5, 6]
# def analyze_numbers(number):
#     sum = 0
#     count = 0
#     for num in number:
#         sum+=num
#         if num%2==0:
#             count+=1
#     avg = sum/len(number)
#     tupleof = (sum, avg, count, )
#     return tupleof
# print(analyze_numbers(numbers))
# # Вывод функции: (21, 3.5, 3)
from itertools import count

# # Задача 2: Работа со строками
# # Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# # и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
# strings = ["apple", "banana", "cherry", "date"]
# def analyze_strings(str):
#     count = 0
#     maxlenword = str[0]
#     minlenword = str[0]
#     for word in str:
#         if len(word)>len(maxlenword):
#             maxlenword = word
#         if len(word)<len(minlenword):
#             minlenword = word
#         for letter in word:
#             if letter == 'a':
#                 count+=1
#                 break
#     tuple_str = (maxlenword, minlenword, count, )
#     return tuple_str
# print(analyze_strings(strings))
# # Вывод функции: ('banana', 'date', 3)


# # Задача 3: Обработка словаря сотрудников
# # Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# # возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
# #
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# def analyze_salaries(employ):
#     sum_salaries = 0
#     avg_salaries = 0
#     name_max = tuple(employ.items())[0][0]
#     max_salaries = employ.get("Alice")
#     # name_max = employees.keys("Alice")
#     for name, salaries in employ.items():
#         sum_salaries+=salaries
#         if salaries > max_salaries:
#             max_salaries = salaries
#             name_max = name
#     avg_salaries = sum_salaries/len(employ)
#     return avg_salaries, max_salaries, name_max
#
# print(analyze_salaries(employees))
# # Вывод функции: (6000.0, 7000, 'Bob')


# # Задача 4: Фильтрация списка
# # Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# # возвращает кортеж из двух списков: четные числа и нечетные числа.
# #
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evenlist = [] #четные
# oddlist = [] #нечетные
# result = (evenlist, oddlist, )
# def filter_numbers(number):
#     for num in number:
#         if num%2==0: evenlist.append(num)
#         else: oddlist.append(num)
#     return result
# print(filter_numbers(numbers))
#
#
# # Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])

# # Задача 1: Генерация словаря
# # Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# # и возвращает словарь, где ключи из первого списка, а значения из второго.
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# def create_dict(keys, values):
#     dict = {key: None for key in keys}
#     count = 0
#     for every in dict:
#         dict[every] = values[count]
#         count+=1
#     return  dict
# print(create_dict(keys,values))
# # Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# Задача 2: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# tuple = {}
# def count_characters(string):
#     for letter in string:
#         if letter not in tuple:
#             tuple.setdefault(letter, 1)
#         # print(tuple[letter])
#         else: tuple[letter]+=1
#     return tuple
# print(count_characters(string))
# # Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# Задача 3: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# chisla = (1, -2, 3, -4, 5)
# pos = []
# neg = []
#
# def summ(*args):
#     sumpos = 0
#     sumneg = 0
#     for num in args:
#         if num>0: sumpos+=num
#         elif num<0: sumneg+=num
#     tuple = (sumpos, sumneg)
#     return tuple
# print(summ(1, -2, 3, -4, 5))
# # Вывод функции: (9, -6)


# Задача 4: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#

# (name="Alice", age=30, city="New York")
# def generate_string(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}={value}', end=' ')
#
# generate_string(name="Alice", age=30, city="New York")

# Вывод функции: name=Alice, age=30, city=New York
