import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    lst = [list((input())) for _ in range(n)]

    for i in range(n):
        for k in range(n - m + 1):
            word = ''
            rv_word = ''
            for j in range(m):
                word += lst[i][j + k]
                rv_word += lst[i][m - j - 1 + k]
            if word == rv_word:
                print(f'#{case} {word}')

    for j in range(n):
        for k in range(n - m + 1):
            word = ''
            rv_word = ''
            for i in range(m):
                word += lst[i + k][j]
                rv_word += lst[m - i - 1 + k][j]
            if word == rv_word:
                print(f'#{case} {word}')