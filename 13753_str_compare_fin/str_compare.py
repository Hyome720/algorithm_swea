import sys

sys.stdin = open('input.txt')

test = int(input())

for case in range(1, test + 1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')