"""
 Сгенерировать список всех простых чисел до  100 с помощью генератора.
"""

number = 100


def is_prime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


lst = [number for number in range(2, 100) if is_prime(number)]
print(lst)
