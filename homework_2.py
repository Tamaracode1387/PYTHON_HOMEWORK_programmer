# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# a = input('Введите вещественное число a: ')
# sum = 0
# for i in a:
#     if i != '.' and i != ',' and i != '-':
#         sum += int(i)
# print(sum)

# или
#
# print(sum([int(i) for i in input() if i.isdigit()]))


########################################################################################################

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# N = int(input())
# fact = 1
# some_list = []
# for i in range(1, N+1):
#     some_list.append(fact*i)
#     fact *= i
# print(some_list)


########################################################################################################

# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int(input())
# summ_ = 0
# for i in range(1, n + 1):
#     summ_ += (1 + 1 / i) ** i
# print(round(summ_, 3))


#########################################################################################################


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.
#

# from random import *
# n = int(input())
# a = int(input())
# b = int(input())
#
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
# print(some_list[a]*some_list[b])


##############################################################################################################################


# 5. Реализуйте алгоритм перемешивания списка.

# import random
#
#
# def newlist(first_list):
#     list = first_list[:]
#     list_length = len(list)
#     for i in range(list_length):
#         index_rand = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[index_rand]
#         list[index_rand] = temp
#     return list
#
#
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# finished_list = newlist(list)
# print(list)
# print(finished_list)
