# 1 Задание

# my_list = (12, 65, 'hello', [1,2,3], True, False, 34)
# def my_type(el):
#     for el in range(len(my_list)):
#         print(type(my_list[el]))
#     return
# my_type(my_list)

# 2 Задание

# el_count = int(input('Ведите количество элементов списка: '))
# my_list = []
# i = 0
# el = 0
# while i < el_count:
#     my_list.append(input('Введите следующее значение списка: '))
#     i += 1
# for elem in range(int(len(my_list)/2)):
#         my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
#         el += 2
# print(my_list)

# 3 Задание

# Season = {'Зима': [1, 12 , 2], 'Весна': [3, 4, 5], 'Лето' :[6, 7, 8], 'Осень': [9, 10 ,11]}
# num  = int(input('Season: '))
# for el in Season:
#     if num in Season[el]:
#         print(el)
#         break
# else:
#     print('Такого месяца не существует')

# 4 Задание

# my_str = input('Введите несколько слов: ')
# my_word = []
# num = 1
# for el in range(my_str.count(' ') + 1):
#     my_word = my_str.split()
#     if len (str(my_word)) <= 10:
#         print(f' {num} {my_word[el]}')
#         num + 1
#     else:
#         print(f' {num} {my_word[el][0:10]}')
#         num += 1

# 5 Задание

# my_list = [8, 6, 5, 4, 3]
# print(f'Рейтинг - {my_list}')
# digit = int(input('Введите число (987 - для выхода) '))
# while digit != 987:
#     for el in range(len(my_list)):
#         if my_list[el] == digit:
#             my_list.insert(el + 1, digit)
#             break
#         elif my_list[0] < digit:
#             my_list.insert(0, digit)
#         elif my_list[-1] > digit:
#             my_list.append(digit)
#         elif my_list[el] > digit and my_list[el + 1] < digit:
#             my_list.insert(el + 1, digit)
#     print(f'текущий список - {my_list}')
#     digit = int(input('Введите число '))




