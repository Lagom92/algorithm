# 숫자 교환 연습하기(최대 상금)
# input
# 3
# 123 1
# 2737 1
# 32888 2

T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()

    # print(num)   # 123
    # print(cnt)

    card = list(num)
    # print(card)   # ['1', '2', '3']

    for i in range(len(card)):   # 교환을 고려할 카드
        for j in range(i, len(card)):   # 자기 자신부터 오른쪽 카드와 교환
            card[i], card[j] = card[j], card[i]
            print(card)
            card[i], card[j] = card[j], card[i]   # 다른 카드와 바꾸기 전에 원상복구

        print()