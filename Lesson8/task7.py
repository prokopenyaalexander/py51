"""
7.	Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO,
если не встречалось.
"""

sequence_of_numbers = input("Введите числа через проблел ")
print(f'Исходная последовательность {sequence_of_numbers}')


def check_numbers(arg):
    temp_dict = {}
    for element in arg.split(" "):
        if element not in temp_dict:
            temp_dict[element] = 1
        else:
            temp_dict[element] += 1
    for key in temp_dict:
        if temp_dict[key] >= 2:
            print(f' Число {temp_dict[key]} - Yes')
        else:
            print(f' Число {temp_dict[key]} - No')


check_numbers(sequence_of_numbers)


