import search_users




def menu():
    while True:
        print()
        print("ПУНКТЫ МЕНЮ:")
        print("1 - Войти")
        print("2 - Выход")
        numb = input("Введите пункт меню: ")
        if numb == "1":
            search_users.read_data_users()

        if numb == "2":
            print("Goodbye!")
            break






