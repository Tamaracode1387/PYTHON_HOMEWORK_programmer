import input_
import import_
import export_
import read_
import add_


def start():
    while True:
        print("")
        print("ПУНКТЫ МЕНЮ:")
        print("1 - Просмотр записей")
        print("2 - Добавление записи")
        print("3 - Экспорт")
        print("4 - Импорт")
        print("5 - Выход из программы")

        number = input("Введите пункт меню: ")

        if number == '1':
            read_.read_func()

        if number == '2':
            info = input_.add()
            add_.add_func(info)

        if number == '3':
             if input_.form() == '1':
                info = input_.exp()
                export_.export_func1(info)
             else:
                info = input_.exp()
                export_.export_func2(info)

        if number == '4':
            if input_.form() == '1':
                import_.import_func1()
            else:
                import_.import_func2()

        if number == '5':
            print("Goodbye!")
            break