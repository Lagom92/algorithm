# 백만 장자 프로젝트
import sys
sys.stdin = open('input03.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case = list(map(int, input().split()))

    case.reverse()

    sell = case[0]
    result = 0
    for i in range(1, N):
        if sell > case[i]:
            result += sell - case[i]
        else:
            sell = case[i]
    print('#{} {}'.format(tc, result))