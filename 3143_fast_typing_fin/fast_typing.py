import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    a, b = input().split()
    cnt = 0
    i = 0

    # 시작 index는 b의 길이를 고려하여 시작
    # for 문을 돌렸더니 banana ana 같은 경우가 나올 경우 ana가 2번 카운트 돼서 while문으로 변경
    while i < len(a) - len(b) + 1:
        # b가 발견될 경우 index 점프
        if a[i:i+len(b)] == b:
            cnt += 1
            i += len(b)
        else:
            i += 1
    fast = len(a) - ((len(b) - 1) * cnt)
    print(f'#{case} {fast}')

