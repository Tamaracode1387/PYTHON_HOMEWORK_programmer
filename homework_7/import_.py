def import_func1():
    filename = input('Введите имя файла, из которого нужно сделать импорт: ')
    with open(filename, 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for line in info_list:
            with open('database.txt', 'a', encoding='utf-8') as d:
                d.write(line + '\n' + '\n')


def import_func2():
    filename = input('Введите имя файла, из которого нужно сделать импорт: ')
    with open(filename, 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for person in info_list:
            person_list = person.split(" ")
            with open('database.txt', 'a', encoding='utf-8') as d:
                for i in person_list:
                    d.write(i + '\n')
                d.write('\n')


