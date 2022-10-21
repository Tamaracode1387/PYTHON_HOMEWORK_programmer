def import_func1(some_person):
    with open('info1.txt', 'a', encoding='utf-8') as f:
        f.write(some_person + '\n')


def import_func2(some_person):
    with open('info2.txt', 'a', encoding='utf-8') as f:
        f.write("\n".join(some_person.split()) + '\n' + '\n')
