def maximumScore(nums, k) -> int:
    p_score = [0] * len(nums)
    max_value = max(nums)
    MOD = 10**9 + 7

    spf = compute_spf(max_value)
    p_score = [get_prime_score(x, spf) for x in nums]

    sorted_q = sorted([(val, idx) for idx, val in enumerate(nums)], reverse=True)
    score = 1
    subarray_counts = compute_subarray_counts(p_score)

    for val, idx in sorted_q:
        if k <= 0:
            break
        subs = subarray_counts[idx]
        if subs >= k:
            score = (score * pow(val, k, MOD)) % MOD
            k = 0
        else:
            score = (score * pow(val, subs, MOD)) % MOD
            k -= subs
    return score % MOD


def compute_spf(n):
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def get_prime_score(x, spf):
    score = 0
    prev = -1
    while x > 1:
        factor = spf[x]
        if factor != prev:
            score += 1
            prev = factor
        x //= factor
    return score


def compute_subarray_counts(p_score):
    n = len(p_score)
    left = [0] * n
    right = [0] * n

    stack = []
    for i in range(n):
        while stack and p_score[stack[-1]] < p_score[i]:
            stack.pop()
        left[i] = stack[-1] + 1 if stack else 0
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and p_score[stack[-1]] <= p_score[i]:
            stack.pop()
        right[i] = stack[-1] - 1 if stack else n - 1
        stack.append(i)

    counts = [(i - left[i] + 1) * (right[i] - i + 1) for i in range(n)]
    return counts


def main():
    nums = [
        52259,
        86735,
        55860,
        30128,
        30123,
        42982,
        15641,
        54403,
        1,
        34410,
        2169,
        27023,
        2401,
        16808,
        27180,
        13566,
        26586,
        94710,
        88133,
        58548,
        43890,
        67758,
        48550,
        12781,
        46410,
        1,
        96162,
        58254,
        46860,
        1,
        1,
        1,
        76560,
        81098,
        67268,
        1,
        30030,
        76385,
        24971,
        1,
        97790,
        10065,
        1,
        68250,
        87665,
        22229,
        36913,
        81510,
        96082,
        93424,
        43890,
        53729,
        1,
        84630,
        78540,
        89870,
        27827,
        81420,
        85470,
        25419,
        62790,
        18940,
        63146,
        68302,
        46410,
        92431,
        1840,
        34710,
        45990,
        6571,
        27960,
        42030,
        57107,
        1,
        5099,
        56385,
        83743,
        43890,
        8813,
        1,
        57910,
        36582,
        60060,
        1,
        92461,
        78540,
    ]

    k = 1717
    print(maximumScore(nums, k))


if __name__ == "__main__":
    main()
