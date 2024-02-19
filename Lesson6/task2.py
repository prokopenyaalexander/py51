"""
2.	Найдите минимальное 9 чисел с помощью функции написанной в предыдущей  задаче. Новую функцию не создавать!
Использовать функцию из предыдущей задачи!
"""


def minimum(*args):
    min_number = 0
    for i in args[0]:
        if min_number > float(i):
            min_number = i
    print(f'Минимальное число {min_number}')


temp_lst = []
print("Введите числа")
for num in range(9):
    number = float(input())
    temp_lst.append(number)

minimum(temp_lst)
