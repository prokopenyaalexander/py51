"""
4.	Дано натуральное число n > 1. Проверьте, является ли оно простым. Простое число – такое, которое делится на себя и на 1.
Единица не простое число! Программа должна вывести слово True, если число простое и False, если число составное.
"""


def is_prime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


num = int(input("Введите число n "))
print(is_prime(num))
