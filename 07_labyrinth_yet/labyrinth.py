from pprint import pprint
import sys

sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def miro(x, y):
    lst[x][y] = 4
    for i in range(4):
        if lst[x + dx[i]][y + dy[i]] == 3:
            return 1
    for i in range(4):
        if lst[x + dx[i]][y + dy[i]] == 0:
            if miro(x + dx[i], y + dy[i]) == 1:
                return 1
    else:
        return 0


for case in range(10):
    test_case = int(input())
    lst = list(list(map(int, (input()))) for _ in range(16))
    for i in range(16):
        for j in range(16):
            if lst[i][j] == 2:
                x, y = i, j

    print(f'#{test_case} {miro(x, y)}')



