"""
Дано двузначное число. Определить является ли сумма его цифр двузначным числом. (Ответ: Да/Нет)
"""

number = int(input("Введите двузначное число "))
if 10 < number > 100:
    print("Неверный ввод")
elif 10 <= ((number // 10) + (number % 10)) < 100:
    print("Да")
else:
    print("Нет")
