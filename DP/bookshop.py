in_list = list(map(int, input().strip().split(" ")))

num_book = in_list[0]
total = in_list[1]

price_list = list(map(int, input().strip().split(" ")))
page_list = list(map(int, input().strip().split(" ")))

dp = [0] * (total + 1)

for index in range(len(price_list)):
    for value in range(total, price_list[index] - 1, - 1):
        if dp[value - price_list[index]] != 0 or value - price_list[index] == 0:
            dp[value] = max(
                dp[value], dp[value - price_list[index]] + page_list[index])

max_page = 0

for index in range(total, -1, -1):
    if dp[index] == 0:
        continue
    else:
        max_page = (dp[index])
        break

print(max_page)
