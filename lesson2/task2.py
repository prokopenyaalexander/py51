"""
Напишите программу, которая выводит True, если хотя бы одно из чисел А, В, С отрицательно. Если нет вывести False. Числа вводятся с клавиатуры в одной строке.
"""

numbers = input("Введите числа ").split(" ")
if int(numbers[0]) < 0 or int(numbers[1]) < 0 or int(numbers[2]) < 0:
    print(True)
else:
    print(False)
