"""
Удалить из текста символы, являющиеся строчными латинскими буквами
"""
test_text = "FGfs"
new_text = ''
letters = []
for letter in range(ord('A'), ord('Z')+1):
    letters.append(chr(letter))

for char in test_text:
    if not (char.isalpha() and char in letters and char.isupper()):
        new_text += char
print(new_text)
