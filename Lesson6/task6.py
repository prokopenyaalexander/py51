"""
Напишите реализацию функции closest_mod_5(x), принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:
-y больше или равно x
-y делится нацело на 5
"""


def closest_mod_5(x):
    temp_x = x * 10
    if x % 5 == 0:
        print(f'Ближайшее кратное 5 числу {x} равно {x}')
    else:
        for value in range(x, temp_x + 1):
            if value >= x and value % 5 == 0:
                print(f'Ближайшее кратное 5 числу {x} равно {value}')
                break


closest_mod_5(13)
