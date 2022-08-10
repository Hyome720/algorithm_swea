import sys

sys.stdin = open('input.txt')

for tests in range(10):
    case = int(input())
    arr = []

    for a in range(100):
        arr.append(list(map(int, input().split())))

    # 행의 합 중 최대값 구하기
    i_max = 0
    for i in range(100):
        i_sum = 0
        for j in range(100):
            i_sum += arr[i][j]
        if i_sum > i_max:
            i_max = i_sum

    # 열의 합 중 최대값 구하기
    j_max = 0
    for j in range(100):
        j_sum = 0
        for i in range(100):
            j_sum += arr[i][j]
        if j_sum > j_max:
            j_max = j_sum

    # 우하단으로 갈 때 합
    r_max = 0
    for i in range(100):
        r_max += arr[i][i]

    # 좌하단으로 갈 때 합
    l_max = 0
    for i in range(100):
        l_max += arr[i][99 - i]

    print(f'#{case} {max(i_max, j_max, r_max, l_max)}')


