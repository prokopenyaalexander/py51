"""
9) Нужно заплатить N рублей. Есть купюры 100, 50, 10, 1 руб. Сколько купюр каждого достоинства нужно отдать покупателю, если он будет платить с самых крупных.
cash = 361
Sample Output :
3 купюры по 100 рублей
1 купюры по 50 рублей
1 купюры по 10 рублей
1 купюры по 1 рублей
"""

cash = 361

hundreds = cash // 100
cash = cash % 100

fifties = cash // 50
cash = cash % 50

tens = cash // 10
cash = cash % 10

ones = cash // 1

print("Sample Output:")
print(f"{hundreds} купюры по 100 рублей")
print(f"{fifties} купюры по 50 рублей")
print(f"{tens} купюры по 10 рублей")
print(f"{ones} купюры по 1 рублей")