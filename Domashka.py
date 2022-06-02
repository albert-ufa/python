# 1 задание

# age = 18
# pensions = 65
# print (pensions - age, 'лет', 'осталось до пенсии')

# the_beginning_of_the_working_day = 8.00
# finishes_work = 17.00
# number_of_working_days_per_week = 5
# print(finishes_work - the_beginning_of_the_working_day, 'Часов длится рабочий день')
# print((finishes_work -the_beginning_of_the_working_day) * 5, 'Рабочих часов в неделю')

# 2 задание
# sec = 987456
# print(sec // 60)
# print(sec // (60 * 60))

# sec = 9825
# hours = sec // 3600
# sec %= 3600
# minute =  sec // 60
# sec %= 60
# seconds = sec % (24 * 3600)
# print(hours, ':', minute,':', sec)

# 3 задание
# User_number = 12
# print((User_number + (User_number * 11)) + User_number * 111)

# 4 задание

# num = abs(int(input('Введите целое положительное число ')))
# max = num % 10
# while num >= 1:
#     num = num // 10
#     if num % 10 > max:
#         max = num % 10
#     if num > 9:
#         continue
#     else:
#         print('Максимальное цифра в числе', max)
#         break

# 5 задание

# profit = float(input('Введиту сумму выручки: '))
# costs = float(input('Введиту сумму издержек: '))
# if profit > costs:
#         print('У вас прибыль')
# elif profit == costs:
#         print('Прибыль равна издержкам! ')
# else:
#         print('У вас убыток!')

# 6 задание

# profit = float(input('Введиту сумму выручки: '))
# costs = float(input('Введиту сумму издержек: '))
# if profit > costs:
#     print('Фирма работает с прибылью')
#     workers = int(input('Введите количество сотрудников: '))
# if profit / workers:
#     print (f'Прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}')

# 7 Задание

# a = int(input('Ведите значение первого дня: '))
# b = int(input('Ведите жедаемый результат в км: '))
# result_days = 1
# result_km = a
# while result_km < b:
#     a = a + 0.1 * a
#     result_days += 1
#     result_km = result_km + a
# print(f'Вы достигнете требуемых результатов на %.f день' % result_days)

