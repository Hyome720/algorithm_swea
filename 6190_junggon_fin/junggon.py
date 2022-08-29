import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    res = -1
    for i in range(N-1):
        for j in range(i+1, N):
            s = lst[i]*lst[j]
            print(s)
            s_ori = lst[i]*lst[j]
            if s < 10:
                continue
            while s >= 1:
                na = s % 10
                s = s//10
                if na < s % 10:
                    break
            else:
                if res < s_ori:
                    res = s_ori
    print(f'#{t} {res}')