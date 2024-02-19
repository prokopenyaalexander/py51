"""
1.	Напишите функцию minimum(a, b, c) - > int, вычисляющую минимум трёх чисел. Функцию min() не использовать!
"""


def minimum(a, b, c):
    if c < a > b:
        print(f'Наибольшее число {a}')
    elif c < b > a:
        print(f'Наибольшее число {b}')
    elif b < c > a:
        print(f'Наибольшее число {c}')



print("Введите числа a, b, c")
number_one = float(input())
number_two = float(input())
number_three = float(input())

minimum(number_one, number_two, number_three)
