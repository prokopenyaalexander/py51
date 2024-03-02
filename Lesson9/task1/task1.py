"""
1.	Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла есть восклицательный знак.
info.txt
"""
path = "/Lesson9/task1/info.txt"


def rewrite_string(arg):
    with open(arg, 'r') as info_file:
        data = info_file.read()
    iter_data = data.split("\n")
    for value in iter_data:
        if "!" in value:
            print(value)


rewrite_string(path)