import sys

sys.stdin = open('input.txt')

test_case = int(input())


def profit(prices):
    max_prices = []
    max_days = []
    max_price = 0
    i = 0
    best_price = [0]
    best_day = [0]
    start = 0
    prof = 0

    # 최고 가격이 이전가격보다 낮아질 경우 그 index와 value 각각 저장
    for idx, value in enumerate(prices):
        if value >= max_price:
            max_price = value
        else:
            max_price = value
            max_days.append(idx - 1)
            max_prices.append(prices[idx - 1])
        # 마지막 날은 무조건 저장
        if idx == len(prices) - 1:
            max_prices.append(value)
            max_days.append(idx)

    max_price = 0

    # 최고가가 있는 날의 index 리스트 만들기
    while i < len(max_prices):
        # 최고가를 계속 갱신하고, 새로운 최고가가 기존의 최고가보다 높다면 pop을 통해 제거
        if max_prices[i] >= max_price:
            best_price.pop()
            best_day.pop()
            while best_price and max_prices[i] >= best_price[-1]:
                best_price.pop()
                best_day.pop()
            max_price = max_prices[i]
            best_price.append(max_price)
            best_day.append(max_days[i])
            i += 1
        # 최고가보다 낮아지면 일단 append해서 다시 진행
        else:
            max_price = max_prices[i]
            best_price.append(max_price)
            best_day.append(max_days[i])
            i += 1

    for i in best_day:
        prof += prices[i] * (i - start) - sum(prices[start:i])
        start = i+1

    return prof


for case in range(1, test_case + 1):
    n = int(input())
    prices = list(map(int, input().split()))

    print(f'#{case} {profit(prices)}')
