"""
Напишите программу, которая выводит True если число Х кратно 3 и заканчивается на 5. Число х вводится с клавиатуры.
"""

number = int(input("Введите число "))
if number % 3 == 0 and str(number)[-1] == '5':
    print(True)
else:
    print(False)

