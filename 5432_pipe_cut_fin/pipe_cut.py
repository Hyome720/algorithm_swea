import sys

sys.stdin = open('input.txt')

test_case = int(input())

# for case in range(1, test_case + 1):
#     pipe = list(input())
#     pipe_lst = []
#     total = 0
#     i = 0
#     while i < len(pipe):
#         if pipe[i] == '(' and pipe[i+1] != ')':
#             pipe_lst.append(1)
#             i += 1
#         elif pipe[i] == '(' and pipe[i+1] == ')':
#             if pipe_lst:
#                 pipe_lst = list(map(lambda x: x + 1, pipe_lst))
#             i += 2
#         else:
#             total += pipe_lst.pop()
#             i += 1
#         print(pipe_lst)
#         print(total)

for case in range(1, test_case + 1):
    pipe = list(input())
    pipe_lst = []
    total = 0
    i = 0
    while i < len(pipe):
        if pipe[i] == '(' and pipe[i+1] != ')':
            pipe_lst.append(1)
            i += 1
        elif pipe[i] == '(' and pipe[i+1] == ')':
            if pipe_lst:
                for j in range(len(pipe_lst)):
                    pipe_lst[j] += 1
            i += 2
        else:
            total += pipe_lst.pop()
            i += 1

    print(f'#{case} {total}')

