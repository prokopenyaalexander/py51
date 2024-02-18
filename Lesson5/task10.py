"""
Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n
"""
number = int(input('Введите число '))
index = 1
temp = 1
while index < number:
    print(f'Число - {index}')
    temp += 1
    index = temp ** 2

