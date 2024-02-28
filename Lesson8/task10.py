"""
10.	Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны. Для введённого слова вывести его синоним или написать что его нет.
"""

dict_of_synonyms = {'худи': 'байка', 'штаны': 'брюки', 'куртка': 'пальто', 'купка': 'шляпа'}


def check_synonim(arg):
    synonim = input("Введите слово ")
    if synonim in arg.keys():
        return f'Синоним для слова {synonim} - {arg[synonim]}'
    else:
        return f'Нет синонима для слова {synonim}'


print(f'Словарь синонимов {dict_of_synonyms}')

print(check_synonim(dict_of_synonyms))
