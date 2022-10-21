def export_func1(last_name):
    with open('info1.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for person in info_list:
            if last_name in person:
                print(person)


def export_func2(last_name):
    with open('info2.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for i in range(0, len(info_list), 5):
            if last_name in info_list[i]:
                print(info_list[i] + '\n', info_list[i + 1] + '\n', info_list[i + 2] + '\n', info_list[i + 3] + '\n')





