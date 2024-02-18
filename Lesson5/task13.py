"""
Дано число n. Найти сумму цифр в этом числе
"""

number = int(input("Введите число "))
sum_of_digits = 0
result = None
if number < 0:
    number = abs(number)
    result = 'Число было отрицательным'

while number != 0:
    sum_of_digits += number % 10
    number //= 10
if result == 'Число было отрицательным':
    sum_of_digits = f'-{sum_of_digits}'
    print(f'Сумма цифр: {sum_of_digits}')
else:
    print(f'Сумма цифр: {sum_of_digits}')
