"""
6.	Даны два списка чисел. Найдите все числа, которые не содержатся одновременно в этих двух списках.
"""
import random
lst1 = [random.randint(1, 4) for el in range(5)]
lst2 = [random.randint(4, 8) for el in range(5)]

print(f'Первый список {lst1}')
print(f'ВТорой список {lst2}')
print(f'Разница 1-го и 2-го {set(lst1) - set(lst2)}')
print(f'Разница 2-го и 1-го {set(lst2) - set(lst1)}')
