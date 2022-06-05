# 1 задание

# def div(*args):
#     try:
#         arg1 = int(input('Велите первое число: '))
#         arg2 = int(input('Ведите второе чиcло: '))
#         res = arg1 / arg2
#     except ValueError:
#         return 'Value error'
#     except ZeroDivisionError:
#         return 'Вы не можете использовать ноль в качестве делителя!'
#     return res
#     '''
#     if arg2 != 0:
#         return arg1 / arg2
#     else:
#         print('Вы не можете использовать ноль в качестве делителя!')
#     '''
# print(f'result  {div()}')

# 2 задание

# '''
#     name = input('Ведите имя: ')
#     surname = input(int('Ведите фамилию: '))
#     year = int(input('Ведите год: '))
#     city = input('Ведите город: ')
#     email = input('Ведите почта: ')
#     telephone = input('Ведите телефон: ')
# '''
# def my_func (имя, фамилия, год, город, почта, телефон):
#      return ' '.join([имя, фамилия, год, город, почта, телефон])
# print(my_func(фамилия = 'Ahmetshin', имя = 'Ravil', год = '1989', город = 'Ufa', почта = 'ahmet_ufa@mail.ru', телефон = '8-987-999-99-24'))

# 3 Задание

# def my_func(arg1 , arg2, arg3):
#     if arg1 >= arg3 and arg2 >= arg3:
#         return arg1 + arg2
#     elif arg1 > arg2 and arg1 < arg3:
#         return arg1 + arg3
#     else:
#         return arg2 + arg3
# print(f'Result - {my_func(int(input("enter first argument: ")), int(input("enter second argument: ")), int(input("enter third argument: ")))}')

# 4 задание

# x = int(input('Ведите число: '))
# y = int(input('Ведите число: '))
# def my_func(x, y):
#     my_func = x ** y
# print(f'my_func - ("x, y")')

# 5 задание

# def my_sum ():
#     sum_res = 0
#     ex = False
#     while ex == False:
#         number = input('Input numbers or Q for quit - ').split()
#         res = 0
#         for el in range(len(number)):
#             if number[el] == 'q' or number[el] == 'Q':
#                 ex = True
#                 break
#             else:
#                 res = res + int(number[el])
#         sum_res = sum_res + res
#         print(f'Current sum is {sum_res}')
#     print(f'Your final sum is {sum_res}')
# my_sum()

# 6 задание

# def int_func (*args):
#     word = input("Input words ")
#     print(word.title())
#     return
# int_func()

