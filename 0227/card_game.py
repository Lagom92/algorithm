# 토너먼트 카드 게임
def find(l, r):
    if l==r:
        return l
    else:
        r1 = find(l, (l+r)//2)
        r2 = find((l+r)//2+1, r)
        if card[r1] == card[r2]:
            return r1
        else:
            if card[r1] == 1 and card[r2] == 3:
                return r1
            elif card[r1] == 3 and card[r2] == 1:
                return r2
            elif card[r1] < card[r2]:
                return r2
            elif card[r1] > card[r2]:
                return r1

import sys
sys.stdin = open('input07.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = [0]+list(map(int, input().split()))           # 인덱스 1번부터 저장

    print(f"#{tc} {find(1,N)}")
