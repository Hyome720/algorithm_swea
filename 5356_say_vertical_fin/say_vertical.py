import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    lst = [list(input()) for _ in range(5)]
    new_word = ''
    max_j = 0

    # i행의 최대 길이 구하기
    for i in range(5):
        if len(lst[i]) > max_j:
            max_j = len(lst[i])

    for j in range(max_j):
        for i in range(5):
            # index j가 i의 길이를 초과하는 경우는 제외
            if len(lst[i]) > j:
                new_word += lst[i][j]

    print(f'#{case} {new_word}')
