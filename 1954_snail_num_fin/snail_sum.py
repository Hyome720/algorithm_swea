import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    end, f_a, f_b = map(int, input().split())
    start = 1
    a = start
    b = end
    a_cnt = 0
    b_cnt = 0
    winner = ''
    while a != f_a & a < f_a:
        a = int((a + end) / 2)
        a_cnt += 1
    else:
        a_cnt = 0
    while b != f_b & b > f_b:
        b = int((b + start) / 2)
        b_cnt += 1
    else:
        b_cnt = 0

    if a_cnt > b_cnt:
        winner = "A"
    elif a_cnt < b_cnt:
        winner = "B"
    else:
        winner = 0

    print(winner)

