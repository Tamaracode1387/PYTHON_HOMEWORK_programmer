import read_homeworks

def student_interface():
   while True:
        print()
        print("Меню:")
        print("1 - Найти домашние задания")
        print("2 - Выйти")
        numb = input("Введите пункт меню: ")
        if numb == "1":
            read_homeworks.read_hw()
        if numb == "2":
            print("Goodbye!")
            break