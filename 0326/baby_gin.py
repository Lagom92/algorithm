# 베이비진 게임
T = int(input())

for tc in range(1, T+1):
    card = list(map(int, input().split()))

    p1 = []
    p2 = []
    res = 0
    for i in range(12):
        if i%2:   # player2
            p2.append(card[i])
            p2.sort()
            print(p2)
        else:
            p1.append(card[i])


    # print(p1)
    # print(p2)
    # print(res)
