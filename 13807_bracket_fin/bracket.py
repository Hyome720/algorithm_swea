import sys

sys.stdin = open('input.txt')


def bracket(word):
    size = len(word)
    lst = []
    # 새로 만들 단어와 기존 단어의 index를 분리
    i = 0
    j = 0
    is_right = 0
    # 기존 단어의 index가 끝날 때까지 반복
    while j < size:
        if i == 0:
            # 기존 입력이 괄호라면 시작
            if word[j] == '(' or word[j] == '{' or word[j] == ')' or word[j] == '}':
                lst.append(word[j])
                i += 1
                j += 1
            # 아니면 word의 index만 증가
            else:
                j += 1
        else:
            # lst에 붙어있는 알파벳이 붙일 알파벳과 같다면 기존 알파벳도 제거하고 인덱스를 재조정
            if (lst[i - 1] == '(' and word[j] == ')') or (lst[i - 1] == '{' and word[j] == '}'):
                del lst[i - 1]
                i -= 1
                j += 1
            elif word[j] == '(' or word[j] == '{' or word[j] == ')' or word[j] == '}':
                lst.append(word[j])
                i += 1
                j += 1
            else:
                j += 1
        if lst:
            is_right = 0
        else:
            is_right = 1
    return is_right

test_case = int(input())

for case in range(1, test_case + 1):
    repeat = list(input())
    print(f'#{case}', bracket(repeat))