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

# 7 задание

# import json
#
# report = []
# with open('text_6.txt', 'r', encoding='UTF-8') as file:
#     text = file.read()
#     file.seek(0)
#     profits = {}
#     profit_sum = 0
#     for row in file:
#         items = row.split(' ')
#         profit = int(items[2]) - int(items[3])
#         if profit > 0:
#             profits.update({items[0]: profit})
#             profit_sum += profit
#     report.append(profits)
#     report.append({'average_profit': (profit_sum / len(profits))})
#
# with open('text_1.json', 'w', encoding='UTF-8') as json_file:
#     json.dump(report, json_file, ensure_ascii=False)
#
# json_report = json.dumps(report, ensure_ascii=False)
#
# print(f"Исходный файл:\n{text}\n")
# print(f"Список:\n{report}\n")
# print(f"json-объект:\n{json_report}")