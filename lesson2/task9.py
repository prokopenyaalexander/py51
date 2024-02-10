"""
Поле  шахматной доски определяется парой натуральных чисел, каждое из которых не превосходит 8
первое – номер вертикали, второе – номер горизонтали. Заданы натуральные числа x1, y1, x2, y2.
Определить, являются ли поля (x1, y1) и (x2, y2) одного  цвета?
На поле (x1, y1) расположен ферзь. Угрожает ли он полю (x2, y2)?
"""

x1 = int(input("Введите x1 координату "))
y1 = int(input("Введите y1 координату "))
x2 = int(input("Введите x2 координату "))
y2 = int(input("Введите y2 координату "))
if (0 < x1 > 8) or (0 < y1 > 8) or (0 < x2 > 8) or (0 < y2 > 8):
    print("Неверный ввод")
if (x1 + y1 + x2 + y2) % 2 == 0:
    print("Поля одного цвета")
else:
    print("Поля разных цветов")
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("Может атаковать")
else:
    print("Не может атаковать")
