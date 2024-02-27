"""
3.	Напишите программу которая вычисляет площадь треугольника по формуле Герона,
однако если пользователь введёт длину хоть одной стороны треугольника равную 0,
то программа должна бросить исключение ArithmeticError.
"""


def calc(side_1, side_2, side_3):
    p = (side_1 + side_2 + side_3) / 2
    return f'Площадь треугольника - {round(p * (p - side_1) * (p - side_2) * (p - side_3), 2)}'


side_one = int(input("Введите сторону a "))
side_two = int(input("Введите сторону b "))
side_three = int(input("Введите сторону c "))
if side_one == 0 or side_two == 0 or side_three == 0:
    raise ArithmeticError("Длина стороны треугольника не может быть равна 0 ")
else:
    print(calc(side_one, side_two, side_three))


