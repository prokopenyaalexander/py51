"""
Дана строка. Преобразовать строку: после каждой буквы 'z' добавить символ '!'.
"""

test_string = 'abzcdz ooozkfxz z'
temp = list(test_string)
for char in temp:
    if char == 'z':
        temp[temp.index('z')] = 'z!'

print(''.join(temp))


