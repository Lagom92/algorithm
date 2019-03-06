# 쉬운 거스름돈
import sys
sys.stdin = open('input02.txt','r')
T = int(input())
for tc in range(1, T+1):
    money = int(input())

    cnt = [0, 0, 0, 0, 0, 0, 0, 0]
    while money >= 10:
        if money >= 50000:
            money -= 50000
            cnt[0] += 1
        elif money < 50000 and money >= 10000:
            money -= 10000
            cnt[1] += 1
        elif money < 10000 and money >= 5000:
            money -= 5000
            cnt[2] += 1
        elif money < 5000 and money >= 1000:
            money -= 1000
            cnt[3] += 1
        elif money < 1000 and money >= 500:
            money -= 500
            cnt[4] += 1
        elif money < 500 and money >= 100:
            money -= 100
            cnt[5] += 1
        elif money < 100 and money >= 50:
            money -= 50
            cnt[6] += 1
        elif money < 50 and money >= 10:
            money -= 10
            cnt[7] += 1
    print('#{}'.format(tc))
    for i in cnt:
        print(i, end=" ")
    print()