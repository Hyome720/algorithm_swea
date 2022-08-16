import sys

sys.stdin = open('input.txt')

test = int(input())

for case in range(1, test + 1):
    str1 = input()
    str2 = input()
    is_in = 0
    for i in range(len(str2) - len(str1) + 1):
        if str2[i:i+len(str1)] == str1:
            is_in = 1
    print(f'#{case} {is_in}')