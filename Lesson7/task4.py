"""
Напишите рекурсивную функцию is_power(n), которая возвращает True, если переданное натуральное число является степенью двойки, и False иначе.
Sample Input:
1048576
Sample Output:
True
"""

def is_power(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return is_power(n // 2)
    else:
        return False


print(is_power(1024))
