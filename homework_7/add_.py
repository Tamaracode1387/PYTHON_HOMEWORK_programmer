def add_func(some_person):
    with open('database.txt', 'a', encoding='utf-8') as f:
        f.write(some_person + '\n')