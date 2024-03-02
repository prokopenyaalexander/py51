"""
5.Создать словарь в качестве ключа которого будет 5-ти значное число, а в качестве значений кортеж состоящий из 2-ух
элементов– имя(str) и возраста(int). Сделать 5-6 элементов словаря и записать данный словарь на диск в файл json формата
"""
import string
import random
import json

alphabet = string.ascii_lowercase


def generate_random_name():
    name = ''.join(random.choice(alphabet) for i in range(10))
    return name


def create_json_file():
    info = {}
    ids = [random.randint(100000, 999999) for _ in range(5)]
    for id_ in ids:
        if id_ not in info:
            info[id_] = (generate_random_name(), random.randint(1,99))
    with open("info", "w") as json_file:
        json.dump(info, json_file, indent=4)

    return json_file


create_json_file()



