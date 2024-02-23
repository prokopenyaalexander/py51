"""
7.	Напишите функцию modify_list(some_lst: list), которая принимает на вход список целых чисел, удаляет из него все
нечётные значения, а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка.
"""


def modify_list(some_lst: list):
    new_lst = []
    for value in some_lst:
        if value % 2 != 0:
            some_lst.remove(value)
    for value in some_lst:
        if value % 2 == 0:
            new_lst.append(value // 2)
        else:
            print("Что-то пошло не так")
    print(new_lst)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
modify_list(lst)
