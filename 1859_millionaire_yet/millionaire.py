import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    start = 0
    max_price = 0
    new_max_price = 0
    i = 0
    profit = 0

    while i < n:
        if prices[i] >= max_price:
            max_price = prices[i]
            i += 1
        else:
            for idx, value in enumerate(prices[i, n]):
                if value >= max_price:
                    max_price = value
                    start = idx
                    i += idx + 1



    print(profit)
    # while i < n:
    #     if prices[i] >= max_price:
    #         max_price = prices[i]
    #         for j in range(i, n):
    #             if max_price < prices[j]:
    #
    #         i += 1
    #     else:
    #         for j in range(start, i):
    #             profit += prices[i]

