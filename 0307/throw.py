# 아름이의 돌 던지기
import sys
sys.stdin = open('input01.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scope = list(map(int, input().split()))

    cnt = 0
    num = 0
    space = []
    for i in range(N):   # 돌과 0 사이의 거리 모음
        di = abs(scope[i] - 0)
        space.append(di)
    minV = min(space)   # 가장 가까운 돌의 거리
    cnt = space.count(minV)   # 가장 가까운 돌의 개수

    print('#{} {} {}'.format(tc, minV, cnt))
