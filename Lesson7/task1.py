"""
1.	Сгенерировать список нечётных двузначных  чисел.
2.	Сгенерировать список из 10 чисел степени 2. От 1 до 10.
3.	Сгенерировать список всех трёхзначных чисел кратных 5 и 3.
4.	Дан список, упорядоченный по не убыванию элементов в нем. Определите, сколько в нем различных элементов.
Set не использовать.
5.	Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же. Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
6.	Создать список используя comprehension. Продублировать все неповторяющиеся элементы.
"""
import random
# Первый пункт
lst1 = [elem for elem in range(15) if elem % 2 != 0]


# Второй пункт
lst2 = [(random.randint(1, 10)) ** 2 for elem in range(10)]


# Третий пункт
lst3 = [elem for elem in range(100, 1000) if elem % 3 == 0 and elem % 5 == 0]


# Четвертый пункт
new_lst = []
lst4 = [(random.randint(1, 10)) for elem in range(10)]
temp_lst = [new_lst.append(elem) for elem in [(random.randint(1, 10)) for elem in range(10)] if elem not in new_lst]
print(f'Исходный массив {lst4}\nНовый массив {new_lst}')


# Пятый пункт
numbers = input("Введите числа/число ").split()
if len(numbers) == 1:
    print(int(numbers[0]))
else:
    result = []
    for i in range(len(numbers)):
        prev_index = i - 1 if i != 0 else len(numbers) - 1
        next_index = i + 1 if i != len(numbers) - 1 else 0
        sum_neighbors = int(numbers[prev_index]) + int(numbers[next_index])
        result.append(sum_neighbors)
    for num in result:
        print(num, end=" ")


# Шестой пункт
lst6 = [(random.randint(1, 5)) for elem in range(10)]
dict_elements = {}
for elem in lst6:
    if elem not in dict_elements:
        dict_elements[elem] = 1
    else:
        dict_elements[elem] += 1
temp_lst = lst6.copy()
for key, val in dict_elements.items():
    if dict_elements[key] < 2:
        lst6.append(key)
print(f'Исходный массив {temp_lst}')
print(f'Измененный массив {lst6}')



