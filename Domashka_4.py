# 1 Задание

# from sys import argv
# name, time, salary, bonus = argv
# try:
#     time = int(time)
#     salary = int(salary)
#     bonus = int(bonus)
#     res = time * salary + bonus
#     print(f'расчёт заработной платы сотрудника {res}')
# except ValueError:
#     print ('Not a number')



# 2 задание

# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# my_new_list = [el for num, el in enumerate (my_list) if my_list[num - 1] < my_list[num]]
# print(f'Исходный список {my_list}')
# print(f'Новый список {my_new_list}')

# 3 задание
# print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

# 4 задание

# my_li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# my_new_li = [el for el in my_li if my_li.count (el) == 1]
# print(f'Новый список {my_new_li}')

# 5 задание

# new = [i for i in range(99, 1000) if i % 2 == 0]
# print(new)

# 6 задание

# from itertools import count
# for el in count(3):
#     if el > 10:
#         break
#     else:
#         print(el)

# from itertools import cycle
#
# c = 0
# for el in cycle('ABC'):
#     if c > 10:
#       break
#     print(el)
#     c += 1

# 7 задание

# from math import factorial
# def fact(n):
#     pr = 1
#     for i in range(1, n + 1):
#         pr = pr * i
#         yield pr
# for el in fact(5):
#     print(el)

