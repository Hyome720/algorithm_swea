import sys

sys.stdin = open('input.txt')

t = int(input())

for t_num in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    diff = a[n-1] - a[0]
    print(f'#{t_num} {diff}')