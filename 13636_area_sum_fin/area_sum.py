import sys

sys.stdin = open('input.txt')

t = int(input())

for t_num in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a_accums = []
    a_sums = []

    # m개의 연속 합의 누적
    for i in range(0, n - m + 1):
        a_sum = 0
        for j in range(i, i + m):
            a_sum += a[j]
        a_sums.append(a_sum)


    # 오름차순으로 정렬
    for i in range(len(a_sums)-1, 0, -1):
        for j in range(0, i):
            if a_sums[j] > a_sums[j+1]:
                a_sums[j], a_sums[j+1] = a_sums[j+1], a_sums[j]

    # 최대 - 최소값 구하기
    maxmin = a_sums[n - m] - a_sums[0]

    print(f'#{t_num} {maxmin}')