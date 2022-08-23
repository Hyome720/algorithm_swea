import sys

sys.stdin = open('input.txt')

test_case = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def miro(x, y):
    lst[x][y] = 4
    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
            if lst[x + dx[i]][y + dy[i]] == 3:
                return 1
    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
            if lst[x + dx[i]][y + dy[i]] == 0:
                if miro(x + dx[i], y + dy[i]) == 1:
                    return 1
    else:
        return 0

for case in range(1, test_case + 1):
    n = int(input())
    lst = list(list(map(int, input())) for _ in range(n))

    for i in range(n):
        for j in range(n):
            if lst[i][j] == 2:
                x, y = i, j
    res = miro(x, y)

    print(f'#{case} {res}')



