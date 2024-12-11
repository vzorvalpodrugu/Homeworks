# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
# Измените элемент "milk" на "almond milk".
# Создайте срез, содержащий первые два элемента списка.
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
# Выведите список покупок, срез и вложенный список.
# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shopping_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]

# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
shopping_list = ['bread', 'milk', 'eggs']
# Измените элемент "milk" на "almond milk".
shopping_list[1] = 'almond milk'
# Создайте срез, содержащий первые два элемента списка.
slice_shopping_list = shopping_list[0:2]  # включается индекс 0 и 1
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
detailed_shopping_list = [
    ['bread', 1.5],
    ['almond milk', 3.0],
    ['eggs', 2.0],
]
# Выведите список покупок, срез и вложенный список.
print(shopping_list)
print(slice_shopping_list)
print(detailed_shopping_list)


# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
student_list = ["Alice","Bob","Charlie","David"]
# Измените имя второго студента на "Eve".
student_list[1] = "Eve"
# Создайте срез, содержащий студентов: "Bob", "Charlie".
student_list_slice = student_list[1:3]
# Создайте вложенный список, где каждый студент имеет список своих оценок.
student_list_marks = [
    ["Alice", [3,4]],
    ["Eve", [2,1]],
    ["Charlie", [4,5]],
    ["David", [2,3]]
]
# Выведите список студентов, срез и вложенный список.
print(student_list)
print(student_list_slice)
print(student_list_marks)
# print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат: [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]



# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4".
tasklist = ["task1","task2","task3","task4"]
# Измените третью задачу на "task3 updated".
tasklist[2] = "task3 updated"
# Создайте срез, содержащий последние две задачи.
tasklist_slice = tasklist[2:]
# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).
tasklist_mark = [
    ["task1", True],
    ["task2", False],
    ["task3 updated", False],
    ["task4", True]
]
print(tasklist)
print(tasklist_slice)
print(tasklist_mark)
# Выведите список задач, срез и вложенный список.
# print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
# print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]
# print(detailed_tasks)  # Ожидаемый результат: [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]



# Упражнение 1: Управление списком фильмов и их рейтингов

# 1.1 Создайте список фильмов, содержащий элементы "Movie1", "Movie2", "Movie3".
films = ["Movie1", "Movie2","Movie3"]

# 1.2 Пропишите условие: добавить в список фильм "Movie4", если его еще нет в списке.
films.append("Movie4")
# 1.3 Пропишите условия: если количество фильмов больше 2, то название второго фильма меняется на "Updated Movie2".
if len(films)>2: films[1]="Updated Movie2"
# Если количество фильмов меньше 5, то объедините имеющийся список с новым списком ["Movie5", "Movie6", "Movie7"]
if len(films)<5: films.extend(["Movie5","Movie6","Movie7"])
# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
filmsfull=[
    ["Movie1",1924, 6.2],
    ["Movie2",2020, 8.1],
    ["Movie3",1924, 6.2],
    ["Movie4",2020, 8.1],
    ["Movie5",1924, 6.2],
    ["Movie6",2020, 8.1],
    ["Movie7",1924, 6.2]
]

# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]

# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
filmsfull.insert(0, ["Movie",2002, 7.7])

# 1.6 Выведите список фильмов и вложенный список.
print(films)
print(filmsfull)
# print(movie_list)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
# print(movie_details)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
# ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]


# Упражнение 2: Анализ списка курсов и их продолжительности

# 2.1 Создайте список курсов, содержащий элементы "Python", "Java", "JavaScript".
course=["Python","Java","JavaScript"]
# 2.2 Добавьте в список курс "C++".
course.append("C++")
# 2.3 Измените название второго курса на "Kotlin".
course[1] = "Kotlin"
# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
if course[0] == "Python" and course[1] == "Kotlin" and course[2] == "JavaScript":
    course_slice = course[:3]
# 2.5 Отсортируйте курсы по названиям.
course.sort()
# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]
course_detail = [
    ["Python", 40],
    ["Kotlin", 30],
    ["JavaScript", 35],
    ["C++", 50]
]
# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
general_hours = course_detail[0][1] + course_detail[1][1] + course_detail[2][1] + course_detail[3][1]
# 2.8 Выведите в консоль:
# - отсортированный список курсо, # Ожидаемый результат:['C++', 'JavaScript', 'Kotlin', 'Python']
print(course)
# - срез, # Ожидаемый результат: ['Python', 'Kotlin', 'JavaScript']
print(course_slice)
# - вложенный список, # Ожидаемый результат: [['Python', 40], ['Kotlin', 30], ['JavaScript', 35], ['C++', 50]]
print(course_detail)
# - общую продолжительность всех курсов. # Ожидаемый результат: 155
print(general_hours)