# 1 задание

# my_f = open('test.txt', 'w')
# line = input('Введите текст \n')
# while line:
#     my_f.writelines(line)
#     line = input('Введите текст \n')
#     if not line:
#         break
#
# my_f.close()
# my_f = open('test.txt', 'r')
# content = my_f.readlines()
# print(content)
# my_f.close()

# 2 задание

# f = open(r'text.txt', 'r', encoding='utf-8')
# line = 0
# for i in f:
#     line += 1
#     flag = 0
#     word = 0
#     for j in i:
#         if j != ' ' and flag == 0:
#             word += 1
#             flag = 1
#         elif j == ' ':
#                 flag = 0
#
#     print(i,len(i),'симв.',word,'сл.')
# print(line,'стр.')
# f.close()

# 3 задание

# with open(r'text.txt', 'r', encoding='utf-8') as my_file:
#     Text = []
#     poor = []
#     my_list = my_file.read().split('\n')
#     for i in my_list:
#         i = i.split()
#         if int(i[1]) < 20000:
#            poor.append(i[0])
#         Text.append(i[1])
# print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, Text)) / len(Text)}')

# 4 задание

# rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# new_file = []
# with open(r'text_2.txt', 'r', encoding='utf-8') as file_obj:
#      for i in file_obj:
#          i = i.split(' ', 1)
#          new_file.append(rus[i[0]] + '  ' + i[1])
#      print(new_file)
#
#
# with open('text_3.txt', 'w', encoding='utf-8') as file_obj_2:
#     file_obj_2.writelines(new_file)

# 5 задание

# def summary():
#     try:
#         with open('text_4.txt', 'w+') as file_obj:
#             line = input('Введите цифры через пробел \n')
#             file_obj.writelines(line)
#             my_numb = line.split()
#
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка в файле')
#     `except ValueError`:
#         print('Неправильно набран номер. Ошибка ввода-вывода')
# summary()

# 6 задание

# with open('text_5.txt', 'r', encoding='UTF-8') as f:
#     text = f.readlines()
#     for line in text:
#         new = ''
#         for el in line:
#             new = ''.join ([new,(el if el in ' 0123456789' else '' )])
#         res = [int(i) for i in new.split()]
#         print(f'{line.split()[0]} - {sum(res)} часов')

# 7 задание

# import json
#
# open('text_6j.json', 'w', encoding='utf-8') as f_write:
# ith open('text_6.txt', 'r', encoding='utf-8') as f_read:
#     profit = {line.split()[0]: int(line.split()[2])-int(line.split()[3]) for line in f_read}
#     res = [profit, {'average_profit': sum([(i) for i in profit.values() if int(i) > 0]) /
#         len([int(i) for i in profit.values() if int(i) > 0])}]
# som.dump(res, f_write)