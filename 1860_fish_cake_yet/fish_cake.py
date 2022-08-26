import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    n, m, k = map(int, input().split())
    guest_lst = list(map(int, input().split()))
    guest_lst.sort()
    t = 1
    cakes = 0
    is_true = 1

    for idx, value in enumerate(guest_lst):
        if value



            
