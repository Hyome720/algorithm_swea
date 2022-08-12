import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    a, b = input().split()
    cnt = len(a.replace(b, "a"))
    print(f'#{case} {cnt}')

