import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    count = 0
    area = int(input())
    bd = list(map(int, input().split()))
    for i in range(2, len(bd)):
           if bd[i-1] < bd[i] and bd[i] > bd[i+1] and bd[i-2] < bd[i] and bd[i] > bd[i+2]:
               a = bd[i] - max([bd[i-2], bd[i-1], bd[i+1], bd[i+2]])
               count += a

    print(f"#{tc} {count}")