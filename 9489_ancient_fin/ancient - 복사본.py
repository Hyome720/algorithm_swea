import sys

sys.stdin = open('input.txt')

test = int(input())

for case in range(1, test + 1):
    N, M = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(N))
    lst_t = list(map(list, zip(*lst)))
    arch = 0


    for i in range(N):
        cnt = 0
        for j in range(M):
            if lst[i][j]:
                cnt += 1
            else:
                arch = max(arch, cnt)
                cnt = 0
        arch = max(arch, cnt)

    for i in range(M):
        cnt_t = 0
        for j in range(N):
            if lst_t[i][j]:
                cnt_t += 1
            else:
                arch = max(arch, cnt_t)
                cnt_t = 0
        arch = max(arch, cnt_t)


    print(f'#{case} {arch}')