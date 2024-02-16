"""
Найти произведение всех целых чисел от 5 до 20 включительно.
"""
multiple = 1
for number in range(5, 21):
    multiple *= number
print(f'Произведение чисел равно: {multiple}')