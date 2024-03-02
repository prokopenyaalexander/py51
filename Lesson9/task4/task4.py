"""
4.	Написать программу “Викторина”. У вас есть 2 файла. В первом содержаться 10 вопросов(каждый вопрос в своей строке)
во втором 10 ответов( каждый ответ как и вопрос в своей строке). Вам нужно считывать по 1 вопросу из файла с вопросами
и давать на них ответ. Если ответ верный, добавлять к счётчику верных ответов 1 балл.
В конце программа выводит количество верных ответов на вопросы.
"""

path = "D:/pyhon/py51/Lesson9/task4/Answers.txt"
path2 = "D:/pyhon/py51/Lesson9/task4/Questions.txt"


def game(arg1, arg2):
    with open(arg2, "r", encoding="utf-8") as quetion:
        quetion_data = quetion.read().rstrip().split("\n")
    with open(arg1, "r") as answers:
        answers_data = answers.read().rstrip().split("\n")
    temp = zip(answers_data, quetion_data)
    data_game = dict(temp)
    cnt = 0
    for quetion, answer in data_game.items():
        print(f'Вопрос {quetion}, ответ {data_game[quetion]}')
        ans = input("Этоверный ответ Да/Нет? ").lower()
        if ans == "да":
            cnt += 1
            print(f'Верных ответов {cnt}')


game(path2, path)
