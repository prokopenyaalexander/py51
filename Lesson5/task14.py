"""
Дано натуральное число n. Найти значение минимальной цифры в данном числе
"""
number = int(input("Введите число "))
min_digit = number % 10
result = None

if number < 0:
    number = abs(number)
    result = 'Число было отрицательным'

while number != 0:
    if min_digit > number % 10:
        min_digit = number % 10
        number = number // 10
    else:
        number = number // 10

if result == 'Число было отрицательным':
    print(f'Минимальная цифра по модулю: {min_digit}')
else:
    print(f'Минимальная цифра числа: {min_digit}')

