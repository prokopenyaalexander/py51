"""
8) Дано число секунд. Вычислите сколько это часов, минут и секунд.
seconds = 4000
Sample Output :
1 час
6 минут
40 секунд

"""
seconds = 4000
hours = seconds // 3600
minutes = (seconds % 3600) // 60
print(f' {hours} час\n {minutes} минут\n {seconds - (hours * 3600 + minutes * 60)} секунд')