import sys

sys.stdin = open('input.txt')

test = int(input())

for case in range(test):
    n, m = input().split()
    m = int(m)
    num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_order = []
    string = list(map(str, input().split()))
    for i in range(len(num_str)):
        for j in string:
            if num_str[i] == j:
                num_order.append(j)
    print(f'#{case + 1}')
    print(*num_order)
