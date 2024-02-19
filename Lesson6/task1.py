"""
1.	Напишите функцию minimum(a, b, c) - > int, вычисляющую минимум трёх чисел. Функцию min() не использовать!
"""


def minimum(*args):
    min_number = 0
    for i in args[0]:
        if min_number > int(i):
            min_number = i
    print(f'Минимальное число {min_number}')


temp_lst = []
print("Введите числа")
for num in range(3):
    number = int(input())
    temp_lst.append(number)

minimum(temp_lst)
