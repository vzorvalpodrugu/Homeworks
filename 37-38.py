#задача1
# x = int(input('Введи число '))
# if x%2==1: print('Нечетное')
# else: print('Четное')

#задача2
# x = int(input('Введи первое число '))
# y = int(input('Введи второе число '))
# z = int(input('Введи третье число '))
# if x>y and x>z: print(f'{x}: максимальное число')
# elif y>x and y>z: print(f'{y}: максимальное число')
# elif z>y and z>x: print(f'{z}: максимальное число')

#задача3
# x = int(input('Введите номер дня недели '))
# match x:
#     case 1:
#         print('Понедельник')
#     case 2:
#         print('Вторник')
#     case 3:
#         print('Среда')
#     case 4:
#         print('Четверг')
#     case 5:
#         print('Пятница')
#     case 6:
#         print('Суббота')
#     case 7:
#         print('Воскресенье')

#задача4
# x = int(input('Введи первую сторону: '))
# y = int(input('Введи вторую сторону: '))
# z = int(input('Введи третью стророну: '))
# if x==y and x==z and y==z: print('Равносторонний')
# elif (x==y and x!=z and y!=z) or (x==z and x!=y and z!=y) or (z==y and z!=x and y!=x):
#     print('Равнобедренный')
# elif x!=y and x!=z and y!=z: print('Разносторонний')

# задача5
# time = int(input('Введите часы: '))
# if time<=4: print('Night')
# elif time>4 and time<10: print('Morning')
# elif time>=10 and time<16: print('Day')
# else: print('Evening')