import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    k, n, m = map(int, input().split())
    gas = list(map(int, input().split()))
    bus = 0
    cnt = 0

    for i in range(len(gas) - 1):
        for j in range(m - i):
            lst = []
            if gas[i+j] - bus <= k and bus < n:
                lst.append(gas[i+j])
            else:
                cnt = 0
            print(lst)

                # if bus + k >= n:
                #     break
                # break

        # elif bus_stop[i] - bus <= k and bus < n:
        #     bus = bus_stop[i]
        #     cnt += 1
        #     if bus + k >= n:
        #         break



    print(f'#{case} {cnt}')
