import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    # 1~12를 지닌 배열 생성
    arr = [0] * 12
    for i in range(1, 13):
        arr[i - 1] = i
    subsets = [[]]
    n_subset = []
    cnt = 0
    n, k = map(int, input().split())
    
    # arr의 부분집합 생성
    for num in arr:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [num])

    # 부분집합 중 원소의 수가 n개인 부분집합만 반환
    for i in range(len(subsets)):
        if len(subsets[i]) == n:
            n_subset.append(subsets[i])

    # n개인 부분집합 중 원소의 합이 k인 부분집합의 수 카운트
    for sub_subset in n_subset:
        sums = 0
        for j in range(n):
            sums += sub_subset[j]
        if sums == k:
            cnt += 1

    print(f'#{case} {cnt}')