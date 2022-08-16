import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    n, q = map(int, input().split())
    boxes = [0] * n

    for i in range(1, q + 1):
        l, r = map(int, input().split())
        new_box = [i] * (r - l + 1)
        boxes[l-1:r] = new_box
    print(f'#{case}', *boxes)