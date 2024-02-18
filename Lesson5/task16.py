"""
Вывести строку, удалив из нее повторные вхождения символов
"""

test_string = "aabcddfff"
print(f'Исходная строка: {test_string}\nПреобразованная строка: {''.join(set(test_string))}')
