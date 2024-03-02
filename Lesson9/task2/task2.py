"""
2.	Создать файл input.txt и записать в него 10 чисел через пробел. Считать из него эти числа.
Затем записать их произведение в файл output.txt.
"""
import random


def rewrite_file(func):
    def wrapper():
        func()
        with open("input.txt", "r+") as file:
            data = file.read().rstrip().split(" ")
        with open("output.txt", "w") as file_output:
            multiple = 1
            for value in data:
                multiple *= int(value)
            file_output.write(str(multiple))
        return file_output
    return wrapper()


@rewrite_file
def create_file():
    lst_numbers = [random.randint(1, 10) for number in range(1, 10)]
    with open("input.txt", "w") as input_file:
        for number in lst_numbers:
            input_file.write(str(number) + " ")






