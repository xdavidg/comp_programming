import time
from collections import Counter
from math import factorial


def countGoodIntegers(n, k):
    total = 0
    odd = True if n % 2 != 0 else False
    unique_str = set()

    ## Finding start and end for palindrome iteration (only consider first half and use createPalindrome to create palindromic second half)
    start = 1
    if odd:
        start *= 10 ** (n // 2)
    else:
        start *= 10 ** (n // 2 - 1)
    end = start * 10

    # Checking all palindromes in [start, end) to see if they are divisible by k
    for num in range(start, end):
        temp = createPalindrome(num, odd)
        if temp % k == 0 and num_to_sorted_string(temp) not in unique_str:
            total += count_unique_permutations(temp)
            unique_str.add(num_to_sorted_string(temp))
    return total


def num_to_sorted_string(num):
    list_str = sorted(str(num))
    return "".join(list_str)


def count_unique_permutations(num):
    str_num = str(num)
    n = len(str_num)

    num_counts = Counter(str_num)

    numerator = factorial(n)

    denominator = 1
    for count in num_counts.values():
        denominator *= factorial(count)

    total = numerator // denominator

    if num_counts.get("0", 0) > 0:
        num_leading_zero = factorial(n - 1)
        denom_leading_zero = 1
        num_counts["0"] -= 1

        for count in num_counts.values():
            denom_leading_zero *= factorial(count)

        total_zeroes = num_leading_zero // denom_leading_zero
        total = total - total_zeroes

    return total


def createPalindrome(num, odd):
    start = num
    reverse = 0
    tens = 1
    if odd:
        num = num // 10
    while num > 0:
        reverse = reverse * 10 + (num % 10)
        tens *= 10
        num = num // 10

    return start * tens + reverse


def main():
    n = 4
    k = 1
    # start = time.time()
    print(countGoodIntegers(n, k))
    # end = time.time()
    # print(end - start)


if __name__ == "__main__":
    main()
