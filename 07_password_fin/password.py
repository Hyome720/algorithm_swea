from pprint import pprint
import sys

sys.stdin = open('input.txt')


for case in range(10):
    test_case = int(input())
    pwd = list(map(int, input().split()))
    i = 1
    while True:
        if i % 5 == 0:
            if pwd[0] - 5 <= 0:
                pwd.pop(0)
                pwd.append(0)
                break
            else:
                pwd[0] -= 5
                pwd.append(pwd.pop(0))
        else:
            if pwd[0] - i % 5 <= 0:
                pwd.pop(0)
                pwd.append(0)
                break
            else:
                pwd[0] -= i % 5
                pwd.append(pwd.pop(0))
        i += 1
    print(f'#{test_case}', *pwd)



