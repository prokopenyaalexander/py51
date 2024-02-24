"""
Дана функция которая запрашивает у пользователя определённые данные для регистрации на портале и запоминает их.
Напишите декоратор, который будет засекать время проведённое пользователем на портале при регистрации.
"""

import datetime


def timerange(func):

    def wrapper():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print(f'Время старта работы - {start_time}')
        print(f'Время финиша работы - {end_time}')
        execution_time = end_time - start_time
        return f'Время работы программы - {execution_time}'
    print(wrapper())


@timerange
def input_creds():
    nickname = input("Введите никнейм(email) ")
    print("Пароль должен содержать минимум 8 символов, 1 заглавную букву и 1 символ !@#")
    password = input("Введите пароль ")
    for ch in password:
        if ch != "!" or ch != "@" or ch != "#" or len(password):
            print("Неверный формат пароля, попробуйте заново")
            break



