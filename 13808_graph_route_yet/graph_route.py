from pprint import pprint
import sys

sys.stdin = open('input.txt')

test_case = int(input())

for case in range(1, test_case + 1):
    v, e = map(int, input().split())
    dic = dict()
    dic = {idx: [] for idx in range(1, v + 1)}
    for _ in range(e):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)
    s, g = map(int, input().split())

    pprint(dic)


