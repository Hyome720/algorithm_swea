from pprint import pprint
import sys

sys.stdin = open('input.txt')

for test in range(10):
    if test>0:
        break
    case, num_node = map(int, input().split())
    # dic1 = {idx: [] for idx in range(100)}
    # dic2 = {idx: [] for idx in range(100)}
    dic1 = dict()
    dic2 = dict()
    nodes = []
    witch = 0
    lst = [0]
    visited = []

    node_list = list(map(int, input().split()))

    for i in range(len(node_list) // 2):
        nodes.append([node_list[i * 2], node_list[(i * 2) + 1]])


    for i in range(num_node):
        if dic1.get(nodes[i][0]):
            dic2[nodes[i][0]] = nodes[i][1]
        else:
            dic1[nodes[i][0]] = nodes[i][1]
    cnt = 0

    while True:
        if dic1.get(witch):
            witch = dic1.get(witch)
            lst.append(witch)
        else:

    # while 1:
    #     if dic1.get(witch):
    #         witch = dic1.get(witch)
    #         lst.append(witch)
    #     else:
    #         del lst[-1]
    #         witch = lst[-1]
    #         dic1[witch] = None
    #         print(witch, dic2.get(witch))
    #         if dic2.get(witch):
    #             witch = dic2.get(witch)
    #             lst.append(witch)
    #         else:
    #             dic2[witch] = None
    #     if witch == 0:
    #         break
    #     cnt += 1
    #     if cnt>20:
    #         break

    print(lst)
    if lst:
        res = 1
    elif 100 in lst:
        res = 0
    print(f'#{case} {res}')


# for test in range(10):
#     case, num_node = map(int, input().split())
#     lst1 = [[] for _ in range(100)]
#     lst2 = [[] for _ in range(100)]
#     nodes = []
#
#     node_list = list(map(int, input().split()))
#     for i in range(len(node_list) // 2):
#         nodes.append([node_list[i * 2], node_list[(i * 2) + 1]])
#
#     for _ in range(num_node):
#     pprint(nodes)