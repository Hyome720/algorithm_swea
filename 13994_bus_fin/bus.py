from collections import deque
import sys

sys.stdin = open('input.txt')


test = int(input())
for case in range(1, test + 1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    bus_stop = [0] * 1001

    for bus in lst:
        if bus[0] == 1:
            for i in range(bus[1], bus[2] + 1):
                bus_stop[i] += 1
        elif bus[0] == 2:
            bus_stop[bus[2]] += 1
            for i in range(bus[1], bus[2], 2):
                bus_stop[i] += 1
        else:
            bus_stop[bus[1]] += 1
            bus_stop[bus[2]] += 1
            if bus[1] % 2:
                for i in range((bus[1] // 3) * 3 + 3, bus[2], 3):
                    if i % 10:
                        bus_stop[i] += 1
                    else:
                        pass
            else:
                for i in range((bus[1] // 4) * 4 + 4, bus[2], 4):
                    bus_stop[i] += 1

    print(f'#{case} {max(bus_stop)}')

