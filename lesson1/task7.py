"""
7) Дан прямоугольник со сторонами a см и b см, сколько квадратов со стороной 30 см можно отрезать от него.
a и b задаются в одной строке с клавиатуры.
side_1 = 150  side_2 = 65
Sample Output :
Можно отрезать 10 квадратов.
"""

side_1 = 165
side_2 = 25
square = 30
result = side_1 * side_2 // 30 ** 2
print(f'Можно отрезать {result} квадратов')
