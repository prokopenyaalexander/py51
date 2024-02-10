"""
Дано 3 числа, вывести большее из них
"""
number_one = float(input("Введите первое число "))
number_two = float(input("Введите второе число "))
number_three = float(input("Введите третье число "))
if number_three < number_one > number_two:
    print(f'Большее число number_three {number_three}')
elif number_three < number_two > number_one:
    print(f'Большее число number_two {number_two}')
elif number_one < number_three > number_two:
    print(f'Большее число number_three {number_three}')
else:
    print("Введены все числа или несколько равных чисел")


