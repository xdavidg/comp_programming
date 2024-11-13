from collections import defaultdict

def main():
    items = [[1,1],[1000000000,1000000000],[2,2],[3,100000]]
    queries = [1,2,3,1000000000]

    prices = list(set(item[0] for item in items))
    prices.sort()
    max_beauty = defaultdict(int)

    for price, beauty in items:
        if max_beauty[price] < beauty:
            max_beauty[price] = beauty
    
    print(prices)

    for i in range(len(prices) - 1):
        if max_beauty[prices[i]] > max_beauty[prices[i + 1]]:
            max_beauty[prices[i + 1]] = max_beauty[prices[i]]

    answers = [0] * len(queries)

    def binary_search(arr, target):
        left, right = 0, len(prices) - 1
        closest = None

        while left <= right:
            mid = (left + right) // 2
            mid_val = arr[mid]

            if mid_val == target:
                return mid_val
            elif mid_val < target:
                closest = mid_val
                left = mid + 1
            else:
                right = mid - 1

        return closest


    for i in range(len(answers)):
        price = binary_search(prices, queries[i])
        answers[i] = max_beauty[price]

    print(answers)
if __name__ == "__main__":
    main()