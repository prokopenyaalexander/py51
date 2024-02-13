"""
Уберите точки из введенного IP-адреса. Выведите сначала четыре числа через пробел, а затем сумму получившихся чисел.
Sample Input:
192.168.0.1
Sample Output:
192 168 0 1
361
"""

test_string = "192.168.0.1"
new_string = test_string.replace('.', ' ')
print(new_string)
print(int(new_string.split(' ')[0]) + int(new_string.split(' ')[1]) + int(new_string.split(' ')[2]) +
      int(new_string.split(' ')[3]))
