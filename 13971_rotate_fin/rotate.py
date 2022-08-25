import sys

sys.stdin = open('input.txt')


t = int(input())

for case in range(1, t + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    k = m % n

    for _ in range(k):
        lst.append(lst.pop(0))
    print(f'#{case} {lst[0]}')