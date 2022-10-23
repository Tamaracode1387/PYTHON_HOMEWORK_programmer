def add_homework():
    lesson = input("К какому уроку добавить задание? ")
    with open('data_homeworks.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for person in info_list:
            if lesson in person:
                home_work = input('Введите домашнее задание ')
                id = str(len(info_list) + 1)
                with open('data_homeworks.txt', 'a', encoding='utf-8') as d:
                    d.write(";".join([id, lesson, home_work]) + '\n')
