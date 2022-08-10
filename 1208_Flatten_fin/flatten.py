import sys

sys.stdin = open('input.txt')

for case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    # dump 수만큼 반복 실행
    for d_case in range(dump):
        # 최대, 최소값을 매번 초기화
        min_box = 100
        max_box = 0
        
        # 최대값보다 클 경우 최대값 변경, index 반환
        for idx, value in enumerate(box):
            if value > max_box:
                max_box = value
                max_idx = idx

        # 최소값보다 작을 경우 최소값 변경, index 반환
        for idx, value in enumerate(box):
            if value < min_box:
                min_box = value
                min_idx = idx
        box[max_idx] -= 1
        box[min_idx] += 1

    # 최대값 - 최소값 반환
    max_n = 0
    min_n = 100
    for i in box:
        if i > max_n:
            max_n = i
        if i < min_n:
            min_n = i

    print(f'#{case} {max_n - min_n}')


