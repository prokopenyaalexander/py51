"""
4.	Дана строка. Проверьте есть ли в ней цифры, иначе бросьте ValueError.
"""


def check_numbers(arg: str):
    temp_lst_for_digits = []
    for char in arg:
        if char.isdigit():
            temp_lst_for_digits.append(char)
    if temp_lst_for_digits:
        print(f'Числа в cтроке есть')
    else:
        raise ValueError("В строке не содержатся числа")


test = input("Введите строку ")
check_numbers(test)



