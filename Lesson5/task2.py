"""
Дано число N. Составить программу выводящую кубы чисел от 1 до N в одну строку.
"""

number = int(input("Введите число "))
for i in range(number):
    print(f'{i**3}', end=" ")
