import sys

sys.stdin = open('input.txt')

def max_bomul(lst):
    global bomul
    global is_true
    # 세로 탐색
    for j in range(m):
        i = 0
        while i < (n - bomul + 1):
            if lst[i][j] == 1:
                k = 1
                while i + k < n and lst[i + k][j] == 1:
                    k += 1
                i += k
                if k == 1:
                    pass
                elif k >= 2:
                    bomul = max(k, bomul)
                    if bomul == n:
                        is_true = 0
                        break
            else:
                i += 1
        if is_true == 0:
            break
        j += 1

    is_true = 1
    # 가로 탐색
    for i in range(n):
        j = 0
        while j < (m - bomul + 1):
            if lst[i][j] == 1:
                k = 1
                while j + k < m and lst[i][j + k] == 1:
                    k += 1
                j += k
                if k == 1:
                    pass
                elif k >= 2:
                    bomul = max(k, bomul)
                    if bomul == m:
                        is_true = 0
                        break
            else:
                j += 1
        if is_true == 0:
            break
        i += 1

    if bomul == 1:
        bomul = 0

    return bomul


test = int(input())

for case in range(1, test + 1):
    n, m = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(m))
    print(lst)
    bomul = 1
    is_true = 1

    print(f'#{case} {max_bomul(lst)}')
