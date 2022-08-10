import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    k, n, m = map(int, input().split())
    bus_stop = list(map(int, input().split()))
    bus = 0
    cnt = 0


    for i in range(len(bus_stop) - 1):
        arr = []
        stop_idx = 0
        for j in range(i+1, len(bus_stop)):
            arr.append(bus_stop[j] - bus_stop[i])
        for idx, value in enumerate(arr):
            if value <= k:
                stop_idx = idx + 1
                bus = bus_stop[stop_idx]


        print(arr)
        # if bus_stop[i+1] - bus <= k and bus < n:
        #     bus = bus_stop[i+1]
        #     cnt += 1
        #     if bus + k >= n:
        #         break
        #
        # elif bus_stop[i] - bus <= k and bus < n:
        #     bus = bus_stop[i]
        #     cnt += 1
        #     if bus + k >= n:
        #         break
        # else:
        #     cnt = 0

    print(f'#{case} {cnt}')
