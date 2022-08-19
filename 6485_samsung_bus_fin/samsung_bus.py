import sys

sys.stdin = open('input.txt')

test_case = int(input())

# for case in range(1, test_case + 1):
#     n = int(input())
#     bus = list(list(map(int, input().split())) for _ in range(n))
#     p = int(input())
#     bus_nums = [0] * p
#
#     for _ in range(p):
#
#     for _ in range(p):
#         c = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    # 정류장 별 토탈 버스의 수를 기록할 배열
    total_bus = [0] * 5000
    # p 주어지면 출력할 배열
    bus_nums = []
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a-1, b):
            total_bus[i] += 1
    p = int(input())
    for _ in range(p):
        c = int(input())
        bus_nums.append(total_bus[c-1])
    print(f'#{case}', *bus_nums)