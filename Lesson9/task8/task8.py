"""
8.	Вашей задачей будет восстановление исходной строки обратно. Напишите программу, которая считывает из файла строку,
соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Для решение вам необходимо открыть файл для чтения 8.txt .
"""

path = "D:/pyhon/py51/Lesson9/task8/8.txt"


def decode(arg):
    letters = []
    numbers = []
    with open(arg, "r") as txt_file:
        data = txt_file.read()
        current_num = ""
        current_letter = ""
        for char in data:
            if char.isdigit():
                current_num += char
            else:
                if current_num:
                    numbers.append(int(current_num))
                    current_num = ""
                if char.isalpha():
                    current_letter += char
        if current_num:
            numbers.append(int(current_num))
        if current_letter:
            letters = list(current_letter)
    temp = zip(letters, numbers)
    results = dict(temp)
    print(results)


decode(path)



