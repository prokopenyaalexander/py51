"""
Необходимо вывести все четные числа на отрезке [a; a * 10]
"""
number = int(input("Введите число а "))
for num in range(number, number * 10 + 1):
    if num % 2 == 0:
        print(f'Четное число - {num}')
