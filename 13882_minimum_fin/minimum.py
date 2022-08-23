import sys

sys.stdin = open('input.txt')


def f(i, r):
    global minsum
    if sum(res[:i]) > minsum:
        return
    if i == r:
        if minsum > sum(res[:r]):
            minsum = sum(res[:r])
        return ans
    for n in range(N):
        if n not in bit[0:i]:
            bit[i] = n
            res[i] = lst[i][n]
            f(i + 1, r)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    bit = [0] * N
    res = [0] * N
    ans = []
    minsum = N * 10
    f(0, N)
    print(f'#{t} {minsum}')



