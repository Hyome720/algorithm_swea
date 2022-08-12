import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    n, k = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    new_lst = []
    num = 0

    for i in range(n):
        num = 0
        for j in range(n):
            if lst[i][j]:
                num += 1
                if j == n - 1:
                    new_lst.append(num)
            else:
                new_lst.append(num)
                num = 0

    for j in range(n):
        num = 0
        for i in range(n):
            if lst[i][j]:
                num += 1
                if i == n - 1:
                    new_lst.append(num)
            else:
                new_lst.append(num)
                num = 0

    print(f'#{case} {new_lst.count(k)}')