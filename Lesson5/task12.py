"""
Дано число n. Определить первую цифру этого числа.
"""

number = int(input("Введите число "))
first_digit = None

while number >= 10:
    number //= 10
first_digit = number
print(f'Первая цифра числа - {first_digit}')
