import sys

sys.stdin = open('input.txt')

def my_max(a, b, c, d):
    tmp = a
    if tmp < b:
        tmp = b
    if tmp < c:
        tmp = c
    if tmp < d:
        tmp = d
    return tmp

for case in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    view = 0

    for i in range(2, n-2):
        n_max = my_max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
        if lst[i] > n_max:
            view += lst[i] - n_max

    print(f'#{case} {view}')

