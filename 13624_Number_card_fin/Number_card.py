import sys

sys.stdin = open('input.txt')

t = int(input())

for t_num in range(1, t+1):
    n = int(input())
    a = input()
    cards = []
    # 숫자를 하나씩 쪼개어 리스트로 반환
    for i in range(0, n):
        card = int(a[i:i+1])
        cards.append(card)

    # 0~9 값의 수를 세기 위한 리스트 생성
    cards_cnt = [0] * 10

    # 인덱스와 맞는 숫자만큼 +1 증가
    for i in range(0, len(cards)):
        cards_cnt[cards[i]] += 1

    # 가장 많은 수를 most에 대입
    most = 0
    for i in range(0, 10):
        if cards_cnt[i] >= most:
            most = cards_cnt[i]

    # cards_cnt 순서를 뒤집고 제일 먼저 나오는 most의 인덱스를 반환
    cards_cnt = cards_cnt[::-1]

    m_num = 9 - cards_cnt.index(most)

    print(f'#{t_num} {m_num} {most}')
