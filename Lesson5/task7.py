"""
Дано натуральное число n. Вывести на экран факториал этого числа
"""

number = int(input("Введите число n "))
muliple = 1
for num in range(1, number):
    muliple *= num
print(f'{muliple}')
