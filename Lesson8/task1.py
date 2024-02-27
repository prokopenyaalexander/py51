"""
1.	Напишите программу которые будет ловить IndexError, когда вы пытаетесь взять индекс элемента, которого нет в списке.
"""
import random
some_lst = [random.randint(1, 20) for value in range(10)]


def check_index(lst):
    try:
        index = int(input("Введите индекс элемнта, который хотите вывести "))
        return f'Массив {lst}\nВведнный индекс {index} - эелемент {lst[index]}'
    except IndexError as error:
        return f'Ошибка - {error}'


print(check_index(some_lst))
