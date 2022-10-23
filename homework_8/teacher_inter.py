import add_hw
import read_homeworks

def teacher_interface():
    while True:
        print()
        print("Меню:")
        print("1 - Посмотреть домашние задания")
        print("2 - Добавить домашнее задание")
        print("3 - Выход")
        numb = input("Введите команду: ")

        if numb == "1":
            read_homeworks.read_hw()
        if numb == "2":
            add_hw.add_homework()
        if numb == "3":
            print("Goodbye!")
            break