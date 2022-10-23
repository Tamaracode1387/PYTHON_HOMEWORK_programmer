def read_hw():
    print()
    with open('data_homeworks.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for line in info_list:
            print(line)