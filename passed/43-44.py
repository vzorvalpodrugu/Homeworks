# Задача 1: Анализ данных о сотрудниках
# У вас есть словарь, содержащий информацию о сотрудниках компании.
# Необходимо провести различные операции с этими данными.

# employees = {
#     "Alice": {"age": 30, "department": "HR", "salary": 5000},
#     "Bob": {"age": 25, "department": "IT", "salary": 6000},
#     "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
# }
#
# # Задание:
# # 1. Выведите имена всех сотрудников.
# # print(employees.keys())
# # 2. Найдите и выведите общую сумму зарплат всех сотрудников.
# salary_sum = 0
# for name, info in employees.items():
#     # print(f'{name} - {info}')
#     salary_sum += info["salary"]
# # print(salary_sum)
#
#
#
# # 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
# employees.setdefault("David", {"age":28, "department":"IT", "salary": 6500})
# # print(employees)
# # 4. Обновите зарплату "Alice" до 5500.
# employees["Alice"]["salary"] = 5500
# # print(employees["Alice"]["salary"])
# # 5. Удалите сотрудника "Charlie".
# employees.pop("Charlie")
# print(employees)
# 6. Выведите данные о каждом сотруднике в формате:
# for every in employees.items():
#     print(f'name:{every[0]} - age:{every[1]["age"]} - department:{every[1]["department"]} - salary:{every[1]["salary"]}')
# # "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
# #


# Задача 2: Управление запасами товаров
# У вас есть словарь, содержащий информацию о запасах товаров в магазине.
# Необходимо провести различные операции с этими данными.
# inventory = {
#     "Apples": {"quantity": 50, "price": 2},
#     "Bananas": {"quantity": 30, "price": 1},
#     "Cherries": {"quantity": 20, "price": 3},
# }
# # Задание:
# # 1. Выведите названия всех товаров.
# print(inventory.keys())
# # 2. Увеличьте количество "Apples" на 10.
# inventory["Apples"]["quantity"]+=10
# # 3. Измените цену "Bananas" на 1.5.
# inventory["Bananas"]["price"]+=1.5
# # 4. Удалите товар "Cherries".
# inventory.pop("Cherries")
#  # 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
# inventory.setdefault("Dates", {"quantity":20, "price": 4})
# # 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).
# sum = 0
# for  key, info in inventory.items():
#     sum+=(info["quantity"]*info["price"])
# print(sum)

# Задача 1: Обработка данных о координатах
# У вас есть список координат, каждая из которых представлена кортежем (x, y).
# Необходимо провести различные операции с этими данными.
# coordinates = [(10, 20), (30, 40), (50, 60)]
# # Задание:
# # 1. Выведите все координаты.
# print(coordinates)
# # 2. Найдите сумму всех координат по оси x и по оси y.
# sumx=0
# sumy=0
# for place in coordinates:
#     sumx+=place[0]
#     sumy+=place[1]
# # 3. Добавьте новую координату (70, 80).
# coordinates+=((70,80),)
# # 4. Замените первую координату на (15, 25).
# coordinates[0]=(15,25)
# # 5. Выведите все координаты, отсортированные по оси x.
# print(coordinates)
# #



# Задача 2: Обработка данных о продуктах
# У вас есть список продуктов, каждый из которых представлен кортежем (название, цена).
# Необходимо провести различные операции с этими данными.
# products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]
# # Задание:
# # 1. Выведите все продукты.
# for name in products:
#     print(name[0])
# # 2. Найдите суммарную стоимость всех продуктов.
# sum=0
# for money in products:
#     sum+=money[1]
# print(sum)
# # 3. Добавьте новый продукт "Date" с ценой 4.
# products+=(("Date", 4),)
# # 4. Замените цену "Apple" на 2.5.
# products[0] = ("Apple", 2.5)
# # 5. Выведите все продукты, отсортированные по цене.
# print(sorted(products, key=lambda x: x[1]))



# # Задача 3: Управление группами пользователей
# # У вас есть множество пользователей, и вам необходимо выполнить различные операции с этими данными.
# users = {"Alice", "Bob", "Charlie"}
# # Задание:
# # 1. Выведите всех пользователей.
# print(users)
# # 2. Добавьте нового пользователя "David".
# users.add("David")
#
# # 3. Удалите пользователя "Bob".
# users.remove("Bob")
#
# # 4. Проверьте, есть ли пользователь "Alice" в множестве.
# print("Alice" in users)
# # 5. Выведите количество пользователей.
# print(len(users))
# #



# # Задача 4: Управление наборами данных
# # У вас есть два множества, представляющих различные наборы данных.
# # Необходимо провести различные операции с этими множествами.
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set3 = {2,3}
# # Задание:
# # 1. Выведите элементы обоих множеств.
# print(set1, set2)
# # 2. Найдите объединение двух множеств.
# print(set1 | set2)
# # 3. Найдите пересечение двух множеств.
# print(set1 & set2)
# # 4. Найдите разность множеств `set1` и `set2`.
# print(set1 - set2)
# # 5. Проверьте, является ли `set2` подмножеством `set1`.
# print(set2 < set1)


