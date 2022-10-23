# читает базу пользователей, ищет по логину, определяет статус пользователя
import student_inter
import teacher_inter


def read_data_users():
    login = input("Введите логин: ")
    with open('data_users.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for person in info_list:
            if login in person:
                if 'student' in person:
                    student_inter.student_interface()
                if 'teacher' in person:
                    teacher_inter.teacher_interface()
            # else:
            #     print("Пользователя под таким логином не существует, попробуйте еще раз!")
            #     break
