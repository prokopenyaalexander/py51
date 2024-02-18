"""
Дан текст. Слова в тексте разделены одним или несколькими пробелами. Написать программу определяющую количество слов, заканчивающихся одной и той же буквой ‘k’
"""
test_text = input("Введите строку ")
temp = test_text.split(" ")
cnt = 0
for letter in temp:
    if letter:
        lst_letter = list(letter)
        if lst_letter[-1] == "k":
            cnt += 1
print(f'Колчество слов {cnt}')
