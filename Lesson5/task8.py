"""
Дано число n. Посчитать сумму всех чётных чисел от 0 до n.
"""
number = int(input("Введите число n "))
sum_of_numbers = 0
while number != 0:
    if number % 2 == 0:
        sum_of_numbers += number
        number -= 1
    else:
        number -= 1
print(sum_of_numbers)
