"""
Удалить в строке все буквы 'b', непосредственно за которыми идет цифра.
"""
test_string = input('Введите строку ')
temp = list(test_string)
for char in temp:
    if char == 'b':
        index = temp.index('b')
        if temp[index + 1].isdigit():
            temp.remove('b')

print(''.join(temp))

