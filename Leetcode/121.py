from collections import deque

prices = [7,1,5,3,6,4]

buy_price = prices[0]
profit = 0

for price in prices[1:]:
    if buy_price > price:
        buy_price = price
    profit = max(profit, price - buy_price)

print(profit)