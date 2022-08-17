import sys

sys.stdin = open('input.txt')

test_case = int(input())

# def pascal(n):
#     i = 0
#     pre_lst = []
#     lst = []
#
#     while i < n:
#         print(lst)
#         if i < 2:
#             lst = [1] * (i + 1)
#             pre_list = lst
#             i += 1
#             return lst
#         else:
#             lst = [1] * (i + 1)
#             for j in range(1, i):
#                 lst[j] = pre_lst[j - 1] + pre_lst[j]
#             pre_lst = lst
#             i += 1
#             return lst

for case in range(1, test_case + 1):
    n = int(input())
    print(f'#{case}')
    lst = []
    pre_lst = []
    for i in range(n):
        if i < 2:
            lst = [1] * (i + 1)
            print(*lst)
        else:
            pre_lst = lst
            lst = [1] * (i + 1)
            for j in range(1, i):
                lst[j] = pre_lst[j - 1] + pre_lst[j]
            print(*lst)
