# 1. Вычислить число c заданной точностью d

# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

# d = str(input('Введите число d, 10^{-1} ≤ d ≤10^{-10}: '))
# k = 1
# summ_ = 0
# for i in range(1000000):
#     if i % 2 == 0:
#         summ_ += 4 / k
#     else:
#         summ_ -= 4 / k
#     k += 2
# print(round(summ_, len(d.split('.')[1])))


#######################################################################################################

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите число: '))
# result = []
# i = 2
# while i <= n:
#     if n % i == 0:
#         result.append(i)
#         n = n / i
#     else:
#         i = i + 1
# print(result)


####################################################################################

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# some_str = input()
# some_list = some_str.split()
# some_int_list = list(map(int, some_list))
# print(some_int_list)
# result = []
# for i in some_int_list:
#     if i not in result:
#         result.append(i)
# print(result)

#################################################################################################
#
# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools
#
#
# k = int(input('Введите степень k: '))
# arg_list = list([randint(0, 101) for i in range(k+1)])
# if arg_list[0] == 0:
#     arg_list[0] = randint(1, 101)
# print(arg_list)
#
# def polynomial(k, arg_list):
#     str1 = ['*x**']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(arg_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
#     print(polynomial)
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     print(polynomial)
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')
#
# list = polynomial(k, arg_list)
# print(list)
#
# # with open('HW4_Polynomial.txt', 'w') as s:
# #     s.write(list)
#
# with open('HW4_Polynomial2.txt', 'w') as s:
#     s.write(list)


##############################################################################################################

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий
# сумму многочленов. Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов
# могут отличаться.

polinom_1 = '5*x^2 + 3*x^6 - 15*x**3 + 66'
polinom_2 = '13*x^3 + 3*x^4 - 15*x^8 - 99'

polinom_1 = polinom_1.replace(' ', '').replace('**', '^').replace('*', '')
polinom_2 = polinom_2.replace(' ', '').replace('**', '^').replace('*', '')


def get_dict_from_polinom(str_pol):
    lst = []
    last_index = -1
    neg = False
    for i, char in enumerate(str_pol):
        if char == '+' or char == '-':
            if neg:
                lst.append('-' + str_pol[last_index + 1:i])
            else:
                lst.append(str_pol[last_index + 1:i])
            last_index = i
            neg = char == '-'
    if neg:
        lst.append('-' + str_pol[last_index + 1:])
    else:
        lst.append(str_pol[last_index + 1:])

    print(lst)
    dct = {}
    for item in lst:
        for i, char in enumerate(item):
            if not char.isdigit() and char != '.' and char != '-':
                dct[item[i:]] = float(item[:i])
                break
        else:
            dct[''] = float(item)

    return dct


dct1 = get_dict_from_polinom(polinom_1)
dct2 = get_dict_from_polinom(polinom_2)

set1 = set(dct1.keys())
set2 = set(dct2.keys())

itog_dct = {}

for key in set1.intersection(set2):
    itog_dct[key] = dct1[key] + dct2[key]

for key in set1.symmetric_difference(set2):
    if key in dct1:
        itog_dct[key] = dct1[key]
    else:
        itog_dct[key] = dct2[key]

print(itog_dct)

print([f'{itog_dct[key]}{key}' for key in sorted(itog_dct.keys(), reverse=True)])





















