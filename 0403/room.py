# 정사각형 방
import sys
sys.stdin = open('input.txt','r')
T = int(input())

def f(i,j):
    global cnt
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = []
    q.append(i)
    q.append(j)

    while q:
        x = q.pop(0)
        y = q.pop(0)

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == arr[x][y] + 1:
                    cnt += 1
                    q.append(nx)
                    q.append(ny)

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]
    res = [0]*(N**2+1)
    maxV = 0
    maxIdx = 0

    for i in range(N):
        for j in range(N):
            cnt = 1
            f(i, j)
            res[arr[i][j]] = cnt

    maxV = max(res)    # 최대값
    maxIdx = res.index(max(res))   # 최대의 인덱스

    print('#{} {} {}'.format(tc, maxIdx, maxV))