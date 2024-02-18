"""
Дано число n. Среди чисел 1, 4, 9, 16, 25, ... найти первое, которые больше n
"""

number = int(input('Введите число '))
index = 1
temp = 1
while index < number:
    temp += 1
    index = temp ** 2
    if index > number:
        print(f'Искомое число - {index}')
        break
