"""
3.	Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние
между точкой (x1, y1) и (x2, y2). Считайте четыре действительных числа и выведите результат работы этой функции.
"""


def distance(x1, y1, x2, y2):
    distance_between_points = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(distance_between_points, 2)


point_x1 = int(input("Введите x1 координату "))
point_y1 = int(input("Введите y1 координату "))
point_x2 = int(input("Введите x2 координату "))
point_y2 = int(input("Введите y2 координату "))

print(distance(point_x1, point_y1, point_x2, point_y2))



