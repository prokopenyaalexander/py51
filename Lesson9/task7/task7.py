"""
7.	Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и
выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое. Для решение вам необходимо открыть файл для чтения 7.txt .
Слова, написанные в разных регистрах, считаются одинаковыми.
"""

path = "D:/pyhon/py51/Lesson9/task7/7.txt"


def cnt_uniq(arg):
    summary = {}
    with open(arg, "r") as txt_file:
        data = txt_file.read().rstrip().split("\n")
    for value in data:
        temp = value.lower().split(" ")
        for val in temp:
            if val not in summary:
                summary[val] = 1
            else:
                summary[val] = + 1
    max_cnt = 1
    for key, value in summary.items():
        if summary[key] >= 1:
            max_cnt = summary[key]
    print(f'Самое частое слово {key}, количетсво раз встретилось в текст - {summary[key]}')


cnt_uniq(path)
