"""
Напишите программу, которая проверяет последнюю цифру числа.
Если последняя цифра числа 3, то вывести True иначе вывести False.
"""

number = input("Введите число ")
last_char = list(str(number))
if int(last_char[-1]) == int(3):
    print(True)
else:
    print(False)



