"""
5.	Дан словарь, который содержит некоторые ключи и значения по этим ключам, пользователь не знает этих ключей.
Бросьте ошибку KeyError в том случае когда пользователь пытается просмотреть значение по ключу, которого нет в словаре.
"""

test_dict = {'a': '1', '2': 'aa', '3': '!'}


def check_key(arg):
    key = input("Введите ключ ")
    if key not in arg.keys():
        raise KeyError("Такой ключ отсутствует в словаре ")


check_key(test_dict)