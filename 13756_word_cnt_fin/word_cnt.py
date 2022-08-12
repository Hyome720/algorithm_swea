import sys

sys.stdin = open('input.txt')

test = int(input())

for case in range(1, test + 1):
    str1 = list(set(input()))
    str2 = list(input())
    max_cnt = 0

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
    print(f'#{case} {max_cnt}')
