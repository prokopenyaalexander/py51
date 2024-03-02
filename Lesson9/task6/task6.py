"""
6.	Прочитать сохранённый json – файл и записать данные на диск в csv файл.
Первое значение каждой строки должно начинаться со слова person, значения разделить ;
"""

import string
import random
import json
import csv

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

path = "D:/pyhon/py51/Lesson9/task5/info.json"


def create_csv_file(arg):
    with open("info", "r") as json_file:
        data = json.load(json_file)
    with open("data_csv.csv", mode="w") as csv_file:
        file_writer = csv.writer(csv_file, delimiter=";", lineterminator="\r")

        for key in data.keys():
            file_writer.writerow(["person", data[key][0], data[key][1]])


create_csv_file(path)
