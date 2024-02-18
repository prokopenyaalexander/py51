"""
Удалить в строке все буквы 'b', непосредственно за которыми идет цифра.
Удалить из текста символы, являющиеся строчными латинскими буквами.
"""
test_string = input('Введите строку ')
temp = list(test_string)
for char in temp:
    if char == 'b':
        index = temp.index('b')
        if temp[index + 1].isdigit():
            temp.remove('b')
print(f'Строка без символа b: {''.join(temp)}')

new_text = ''
letters = []
for letter in range(ord('A'), ord('Z')+1):
    letters.append(chr(letter))

for char in test_string:
    if not (char.isalpha() and char in letters and char.isupper()):
        new_text += char
print(f'Измененный текст {new_text}')

