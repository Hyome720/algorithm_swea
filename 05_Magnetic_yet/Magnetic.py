from pprint import pprint
import sys

sys.stdin = open('input.txt')

# 1 아래로
# 2 위로


def magnetic(table):
    cnt = 0
    for j in range(100):
        drop = 0
        i = 0
        while i < 100:
            if table[i][j] == 0:
                i += 1
            elif drop == 0 and table[i][j ] == 1:
                drop = 1
                i += 1
            elif drop == 1 and table[i][j] == 2:
                drop = 0
                cnt += 1
                i += 1
            else:
                i += 1
    return cnt

for case in range(1, 11):
    n = int(input())
    table = list(list(map(int, input().split())) for _ in range(100))
    cnt = 0

    print(f'#{case} {magnetic(table)}')
