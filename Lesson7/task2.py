"""
7.	Дана функция, которая выводит все простые числа в промежутке от 1 до 100.
Написать декоратор который будет проверять время работы этой функции.
Задекорировать функцию. Вывести время работы этой функции, а так же сами простые числа.
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
def print_primes():
    for num in range(2, 11111):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
