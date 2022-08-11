import sys

sys.stdin = open('input.txt')

test = int(input())

for case in range(1, test + 1):
    n = int(input())
    a = list(map(int, input().split()))
    # input a를 오름차순으로 정렬
    a.sort()
    odd_arr = [0] * n
    even_arr = [0] * n
    spc_arr = []

    for i in range(n):
        # n / 2 기준 좌측의 작은 수는 index 1부터 2씩 증가하는 index에 배치
        if i < n / 2:
            odd_arr[i * 2 + 1] = a[i]
        # n / 2 기준 우측의 큰 수는 index 0부터 2씩 증가하는 index에 역순으로 배치
        if i >= n / 2:
            even_arr[(n - 1 - i) * 2] = a[i]

    # arr를 써서 0인 값을 서로 상충
    for i in range(10):
        spc_arr.append(odd_arr[i]|even_arr[i])

    print(f'#{case}', *spc_arr)