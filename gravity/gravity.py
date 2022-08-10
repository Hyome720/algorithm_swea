import sys

sys.stdin = open('input.txt')

lst = list(map(int, input().split()))

for idx in range(len(lst)):
    value = lst[idx]
    # 나보다 작은 박스무더기의 수
    cnt = 0 # 하나식 더해
    나보다 오른쪽에 있는
    for right_idx in range(idx+1, len(lst)):
        if value > lst[right_idx]:
            cnt += 1
