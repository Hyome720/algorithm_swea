import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    cnt = 0
    a, b, c, d, e = 0, 0, 0, 0, 0
    while n % 2 ** (a + 1) == 0:
        a += 1
    while n % 3 ** (b + 1) == 0:
        b += 1
    while n % 5 ** (c + 1) == 0:
        c += 1
    while n % 7 ** (d + 1) == 0:
        d += 1
    while n % 11 ** (e + 1) == 0:
        e += 1


    print(f'#{case} {a} {b} {c} {d} {e}')
