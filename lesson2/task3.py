"""
Верно ли что, целые n и k имеют одинаковую четность.
"""

n = int(input("Введите n "))
k = int(input("Введите k "))
if n % 2 == k % 2:
    print("Yes")
else:
    print("No")
