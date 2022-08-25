from collections import deque
import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    q = deque()
    for idx, n in enumerate(range(N), start=1):
        q.append([idx, C[n]])
    idx = N
    while len(q) > 1:
        print(q)
        q[0][1] = q[0][1] // 2
        if q[0][1] == 0:
            q.popleft()
            if idx < len(C):
                q.append([idx + 1, C[idx]])
                idx += 1
        else:
            q.append(q.popleft())
    print(f'#{t} {q[0][0]}')