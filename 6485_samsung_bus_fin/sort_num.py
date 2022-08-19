import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(f'#{case}', *nums)