"""
Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения.
Если буква f в данной строке встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
"""
test_string = input("Введите строку ")
if test_string.count('f') == 1:
    print("-1")
elif test_string.count('f') >= 2:
    first_occurrence = test_string.find('f')
    second_occurrence = test_string.find('f', first_occurrence + 1)
    print(second_occurrence)
elif test_string.count('f') == 0:
    print(-2)

