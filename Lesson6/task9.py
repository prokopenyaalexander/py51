"""
Задано два списка. Написать функцию которая находит наименьший элемент среди элементов первого списка,
которые не входит во второй список.
"""

lst1 = [1, 4, 6, 7, -99, 99, 9, 2]
lst2 = [2, 3, 6, 4, 7, 99, 51, 3]


def minimal_element(a, b):
    lst_minimal = []
    for element in a:
        if element not in b:
            lst_minimal.append(element)
    return f'Минимальный элемент среди элементов не входящих во второй список {min(lst_minimal)}'


print(minimal_element(lst1, lst2))

