"""
8.	В ходе исследований ученые делают некие замеры, результаты которых заносят в базу данных.
Однако для анализа результатов нет необходимости держать в базе "лишние", повторяющиеся данные.
Напишите программу, которая выводит максимальное количество записей, после удаления которых анализ
результатов будет произведен верно. Список элементов вводится через пробел.
"""

sequence_of_data = input("Введите данные через пробел ")
print(f'Исходная последовательность {sequence_of_data}')


def check_results(arg):
    return (f'Максимальное количество записей, после удаления которых анализ результатов будет произведен верно'
            f'\n{len(sequence_of_data.split(" ")) - len(set(sequence_of_data.split(" ")))}')


print(check_results(sequence_of_data))
