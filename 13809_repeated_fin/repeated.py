import sys

sys.stdin = open('input.txt')


def rp_word(word):
    size = len(word)
    lst = []
    # 새로 만들 단어와 기존 단어의 index를 분리
    i = 0
    j = 0
    # 기존 단어의 index가 끝날 때까지 반복
    while j < size:
        if i == 0:
            # 붙어있는 알파벳이 중복이면 index 건너뜀
            if word[j] == word[j + 1]:
                j += 2
            # 중복 아니면 그제서야 append
            else:
                lst.append(word[j])
                i += 1
                j += 1
        else:
            # lst에 붙어있는 알파벳이 붙일 알파벳과 같다면 기존 알파벳도 제거하고 인덱스를 재조정
            if lst[i - 1] == word[j]:
                del lst[i - 1]
                i -= 1
                j += 1
            else:
                lst.append(word[j])
                i += 1
                j += 1
    return len(lst)

test_case = int(input())

for case in range(1, test_case + 1):
    repeat = list(input())
    print(f'#{case}', rp_word(repeat))
