"""
Дано натуральное число. Определить произведение цифр в нем которые кратны 2, кроме числа 0.
"""
number = list(str(input('Введите число ')))
multiple = 1
index = 0
while index != len(number):
    if int(number[index]) % 2 == 0 and int(number[index]) != 0:
        multiple *= int(number[index])
        index += 1
    else:
        index += 1
print(f'Произведение равно - {multiple}')

