# Темы: Операции над строками, Индексы и срезы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Объедините строки "Hello" и "London" без пробела. Ожидаемый результат: "HelloLondon"
print('Hello' + 'London')

# 2. Выведите последний символ строки "Programming". Ожидаемый результат: "g"
x = 'Programming'
print(x[10])

# 3. Дублируйте строку "Hi" три раза. Ожидаемый результат: "HiHiHi"
print('Hi'*3)

# 4. Определите длину строки "Artificial Intelligence".
y='Artificial Intelligence'
print(len(y))

# 5. Объедините строки "Good" и "Morning" с запятой между ними. Ожидаемый результат: "Good,Morning"
print('Good' + ',' + 'Morning')

# 6. Создайте срез строки "Natural Language Processing" со значением "nguag".
x6 = 'Natural Language Processing'
print(x6[10:15])
# 7. Объедините строки "Data" и "Science" с дефисом между ними. Ожидаемый результат: "Data-Science"
print('Data' + '-' + 'Science')

# 8. Объедините строки "AI" и "ML" с двоеточием между ними. Ожидаемый результат: "AI:ML"
print('AI' + ':' + 'ML')

# 9. Дублируйте строку "Test" шесть раз. Ожидаемый результат: "TestTestTestTestTestTest"
print('Test'*6)

# 10. Выведите первый символ строки "Python". Ожидаемый результат: "P"
x10 = 'Python'
print(x10[0])

# 11. Создайте срез строки "Hello, Anna!" от 0 до 5. Ожидаемый результат: "Hello"
x11 = 'Hello, Anna!'
print(x11[0:5])

# 12. Определите длину строки "Natural Language Processing".
x12 = 'Natural Language Processing'
print(len(x12))

# 13. Выведите второй символ строки "Лето". Ожидаемый результат: "е"
x13 = 'Лето'
print(x13[1])

# 14. Выведите предпоследний символ строки "Machine Learning". Ожидаемый результат: "n"
x14 = 'Machine Learning'
print(x14[-2])

# 15. Дублируйте строку "Yes" четыре раза. Ожидаемый результат: "YesYesYesYes"
print('Yes'*4)

# 16. Создайте срез строки "Deep Learning" со значением "ep Le".
x16 = 'Deep Learning'
print(x16[2:7])

# 17. Выведите третий символ строки "Computer Vision". Ожидаемый результат: "m"
x17 = 'Computer Vision'
print(x17[2])

# 18. Определите длину строки "Deep Learning". Ожидаемый результат: 13
print(len('Deep Learning'))

# 19. Объедините строки "Python" и "Rocks" с пробелом между ними. Ожидаемый результат: "Python Rocks"
print('Python' + ' ' + 'Rocks')

# 20. Создайте срез строки "Data Science" со значением "cien".
print('Data Science'[-6:-2])

# 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# Ожидаемый результат: "HOW ARE YOU?"
print('hOw aRe yOu?'.upper())

# 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".
print('Bananas are amazing!'.count('a'))

# 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# Ожидаемый результат: "python programming"
print('PYTHON PROGRAMMING'.lower())

# 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# Ожидаемый результат: "Discover new worlds   "
print('   Discover new worlds   '.lstrip())

# 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# Ожидаемый результат: "It was a sunny day."
print('It was a rainy day.'.replace('rainy','sunny'))

# 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".
print('Innovation drives progress.'.find('innovation'))

# 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# Ожидаемый результат: "   Explore the universe"
print('   Explore the universe   '.rstrip())

# 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".
print('The Milky Way galaxy is vast.'.find('galaxy'))

# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]
print('Apple;Banana;Cherry;Date'.split(';'))

# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."
print('In the future, robots will rule the world.'.replace('robots','humans'))

# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"
print('artificial intelligence'.title())


# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]
print('Python is a versatile language'.split())

# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"
print('   Learn Python   '.strip())


