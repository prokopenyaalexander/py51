"""
10) Улитка ползет по вертикальному шесту высотой h метров, поднимаясь за день на x метров, а за ночь спускаясь на y метров. На какой день улитка доползет до вершины шеста?
"""
h = 10
x = 3
y = 2

distance_day_and_night = x - y
days = (h - x) // distance_day_and_night + ((h - x) % distance_day_and_night) // (x - y)
days += 1
print(f"Улитка доползет до вершины шеста на {days} день/дней")

