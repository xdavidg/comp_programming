import sys

def coin_change(amount, coins):
    total = amount + 1
    dp = [total] * (amount + 1)
    dp[0] = 0

    for c in coins:
        for a in range(c, amount + 1):
            if dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1

    return -1 if dp[amount] == total else dp[amount]

def main():
    in_list = list(map(int, input().strip().split(" ")))
    amount = in_list[0]
    num_coin = in_list[1]

    coins = list(map(int, input().strip().split(" ")))

    print(coin_change(amount, coins))

if __name__ == "__main__":
    main()
