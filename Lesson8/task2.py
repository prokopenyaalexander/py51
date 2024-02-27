"""
2.	Напишите программу которые будет ловить TypeError, когда вы пытаетесь скаткатенировать строку и число.
"""
import random


lst = [int(input("Введите число ")), input("Введите строку ")]
choice = random.choice(lst)


def concat(arg: str):
    some_string = 'some_string'
    try:
        return f'{arg + some_string}'
    except TypeError:
        return f'Введный эелемент - {arg} не соответствует типу строка.\nОшибка {TypeError}'


print(concat(choice))
