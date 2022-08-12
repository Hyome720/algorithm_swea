import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    fly_max = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            fly = 0
            for a in range(m):
                for b in range(m):
                    fly += lst[i + a][j + b]
            if fly > fly_max:
                fly_max = fly
    print(f'#{case} {fly_max}')