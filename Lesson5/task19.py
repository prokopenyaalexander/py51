"""
С клавиатуры вводится натуральное число n <= 1000. Выведите n строк вида "На лугу n коров", склоняя слово "коров" в соответствии с числом n. Проверяем большие числа!!!
Sample Input:
5
Sample Output:
На лугу 1 корова
На лугу 2 коровы
На лугу 3 коровы
На лугу 4 коровы
На лугу 5 коров
"""
number = 101 #int(input("введите число "))
dict_of_cows = {0: "коров", 1: "корова", 2: "коровы", 3: "коровы", 4: "коровы", 5: "коров", 6: "коров", 7: "коров", 8: "коров", 9: "коров"}
if number < 20:
    while number != 0:
        if number < 10:
            for key, value in dict_of_cows.items():
                if number == key:
                    print(f'На лугу {number} {dict_of_cows[key]}')
        else:
            print(f'На лугу {number} коров')
        number -= 1
else:
    while number != 0:
        temp = number % 10
        for key, value in dict_of_cows.items():
            if temp == key:
                print(f'На лугу {number} {dict_of_cows[key]}')
        number -= 1


