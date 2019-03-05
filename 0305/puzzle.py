# 어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open('input01.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]

    cnt = 0
    for i in range(N):   # 가로 검색
        a = 0
        for j in range(N):
            if arr[i][j] == 1:
                a += 1
            else:
                if a == K:
                    cnt += 1
                    a = 0
                else:
                    a = 0
        if a == K:
            cnt += 1

    for i in range(N):   # 세로 검색
        b = 0
        for j in range(N):
            if arr[j][i] == 1:
                b += 1
            else:
                if b == K:
                    cnt += 1
                    b = 0
                else:
                    b = 0
        if b == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
