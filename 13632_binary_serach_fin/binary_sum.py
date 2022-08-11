import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    end, f_a, f_b = map(int, input().split())
    start = 1
    # a, b의 초기 위치 설정
    a = end / 2
    b = end / 2
    # a, b의 시작점 각각 설정
    a_s = start
    a_e = end
    b_s = start
    b_e = end
    # 초기 위치를 설정해주었음으로 카운트를 1부터 시작
    a_cnt = 1
    b_cnt = 1
    winner = ''

    # a가 찾는 경우
    while a != f_a:
        if a < f_a:
            # a의 위치를 start와 end 의 중간 지점으로 반환
            a = int((a_s + a_e) / 2)
            a_cnt += 1
            # a의 위치가 찾고자하는 위치보다 크다면 끝점을 a로 반환
            if a > f_a:
                a_e = a
            # a의 위치가 찾고자하는 위치보다 작다면 시작점을 a로 반환
            elif a < f_a:
                a_s = a
        elif a > f_a:
            a = int((a_s + a_e) / 2)
            a_cnt += 1
            if a > f_a:
                a_e = a
            elif a < f_a:
                a_s = a

    # b가 찾는 경우
    while b != f_b:
        if b < f_b:
            b = int((b_s + b_e) / 2)
            b_cnt += 1
            if b > f_b:
                b_e = b
            elif b < f_b:
                b_s = b
        elif b > f_b:
            b = int((b_s + b_e) / 2)
            b_cnt += 1
            if b > f_b:
                b_e = b
            elif b < f_b:
                b_s = b


    if a_cnt > b_cnt:
        winner = "B"
    elif a_cnt < b_cnt:
        winner = "A"
    else:
        winner = 0

    print(f'#{case} {winner}')

