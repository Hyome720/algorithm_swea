import sys

sys.stdin = open('input.txt')

test = int(input())

for case in range(1, test + 1):
    n, m = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))

    fly_max = 0

    for i in range(n):
        for j in range(n):
            fly_sum_x = lst[i][j]
            fly_sum_t = lst[i][j]
            k = 1
            while k < m:
                if i + k < n and j + k < n:
                    fly_sum_x += lst[i + k][j + k]
                if i + k < n and j - k >= 0:
                    fly_sum_x += lst[i + k][j - k]
                if i - k >= 0 and j + k < n:
                    fly_sum_x += lst[i - k][j + k]
                if i - k >= 0 and j - k >= 0:
                    fly_sum_x += lst[i - k][j - k]
                k += 1
            l = 1
            while l < m:
                if i + l < n:
                    fly_sum_t += lst[i + l][j]
                if i - l >= 0:
                    fly_sum_t += lst[i - l][j]
                if j + l < n:
                    fly_sum_t += lst[i][j + l]
                if j - l >= 0:
                    fly_sum_t += lst[i][j - l]
                l += 1
            fly_max = max(fly_sum_x, fly_sum_t, fly_max)

    print(f'#{case} {fly_max}')