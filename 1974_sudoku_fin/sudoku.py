from pprint import pprint
import sys

sys.stdin = open('input.txt')

test_case = int(input())


def is_soduku(sudoku):
    exit_loop = False
    is_true = 1

    # 가로축 검사
    for i in range(9):
        if len(set(sudoku[i])) != 9:
            exit_loop = True
            is_true = 0
            break
    if exit_loop:
        return is_true

    # 세로축 검사
    for j in range(9):
        sero = []
        for i in range(9):
            sero.append(sudoku[i][j])
        if len(set(sero)) != 9:
            exit_loop = True
            is_true = 0
            break
    if exit_loop:
        return is_true

    # 3 x 3 검사
    for _ in [0, 3, 6]:
        for _ in [0, 3, 6]:
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(sudoku[i][j])
            if len(set(box)) != 9:
                exit_loop = True
                is_true = 0
                break
        if exit_loop:
            break

    return is_true

for case in range(1, test_case + 1):
    sudoku = list(list(map(int, input().split())) for _ in range(9))

    print(f'#{case} {is_soduku(sudoku)}')


