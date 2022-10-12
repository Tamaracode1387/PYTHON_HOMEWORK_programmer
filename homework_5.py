# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

## вариант 1:
# some_text = 'Ученье крабв - свет, абвритура а шкоабвла неученье - тьма даабв'.split()
# print(' '.join([word for word in some_text if 'абв' not in word]))


###################################################################################################################################

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

## человек с человеком:
# from random import randint

# def take(name):
#     x = int(input(f"{name}, ты можешь взять от 1 до 28 конфет, сколько возьмешь?: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, столько нельзя, ещё раз: "))
#     return x

# def result_step(name, k, count, summ):
#     print(f"{name} взял {k} конфет, итого у него {count}. Всего на столе осталось {summ} конфет.")

# player1 = input("Имя первого игрока: ")
# player2 = input("Имя второго игрока: ")
# summ = int(input("Количество конфет на столе: "))
# flag = randint(0,2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# count1 = 0
# count2 = 0

# while summ > 28:
#     if flag:
#         k = take(player1)
#         count1 += k
#         summ -= k
#         flag = False
#         result_step(player1, k, count1, summ)
#     else:
#         k = take(player2)
#         count2 += k
#         summ -= k
#         flag = True
#         result_step(player2, k, count2, summ)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


## человек с ботом:
# from random import randint

# def take(name):
#     x = int(input(f"{name}, ты можешь взять от 1 до 28 конфет, сколько возьмешь?: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, столько нельзя, ещё раз: "))
#     return x

# def result_step(name, k, count, summ):
#     print(f"{name} взял {k} конфет, итого у него {count}. Всего на столе осталось {summ} конфет.")

# player1 = input("Имя игрока: ")
# player2 = ('Бот')
# summ = int(input("Количество конфет на столе: "))
# flag = randint(0,2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# count1 = 0
# count2 = 0

# while summ > 28:
#     if flag:
#         k = take(player1)
#         count1 += k
#         summ -= k
#         flag = False
#         result_step(player1, k, count1, summ)
#     else:
#         k = randint(0,29)
#         count2 += k
#         summ -= k
#         flag = True
#         result_step(player2, k, count2, summ)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# ## человек с умным ботом:
# from random import randint

# def take(name):
#     x = int(input(f"{name}, ты можешь взять от 1 до 28 конфет, сколько возьмешь?: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, столько нельзя, ещё раз: "))
#     return x

# def result_step(name, k, count, summ):
#     print(f"{name} взял {k} конфет, итого у него {count}. Всего на столе осталось {summ} конфет.")

# player1 = input("Имя игрока: ")
# player2 = ('Бот')
# summ = int(input("Количество конфет на столе: "))
# flag = randint(0,2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# count1 = 0
# count2 = 0

# while summ > 28:
#     if flag:
#         k = take(player1)
#         count1 += k
#         summ -= k
#         flag = False
#         result_step(player1, k, count1, summ)
#     else:
#         k = randint(0,29)
#         count2 += k
#         summ -= k
#         flag = True
#         result_step(player2, k, count2, summ)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


################################################################################################################################

# 3. Создайте программу для игры в ""Крестики-нолики"".

# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")


###############################################################################################################################

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


# def coding(text):
#     count = 1
#     result = ''
#     for i in range(len(text)-1):
#         if text[i] == text[i+1]:
#             count += 1
#         else:
#             result = result + str(count) + text[i]
#             count = 1
#     if count > 1 or (text[len(text)-2] != text[-1]):
#         result = result + str(count) + text[-1]
#     return result

# def decoding(text):
#     number = ''
#     result = ''
#     for i in range(len(text)):
#         if not text[i].isalpha():
#             number += text[i]
#         else:
#             result = result + text[i] * int(number)
#             number = ''
#     return result

# text = input("Введите текст для сжатия: ")
# print(f"Текст после кодировки: {coding(text)}")
# print(f"Текст после дешифровки: {decoding(coding(text))}")