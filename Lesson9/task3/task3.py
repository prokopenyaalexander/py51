"""
3.	Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара, цену единицы.
Вывести список товаров стоимость которых превышает 1 000 000 р.
"""
path = "D:/pyhon/py51/Lesson9/task3/goods.txt"


def cost(arg):
    goods_and_cost = {}
    with open(arg, "r") as input_file:
        data = input_file.read().rstrip().split("\n")
    for value in data:
        temp_value = value.split(" ")
        goods_and_cost[temp_value[0]] = {'Количество': temp_value[1], 'Цена': temp_value[2]}
    for key, value in goods_and_cost.items():
        cnt = int(list(goods_and_cost[key].values())[0])
        price = int(list(goods_and_cost[key].values())[1])
        if cnt * price > 1000000:
            print(f'Наименование -  {key}')


cost(path)


