# 오셀로
# 
import sys
sys.stdin = open('input01.txt','r')
T = int(input())

def check(x,y):
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [1, 1, 1, 0, -1, -1, -1, 0]
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and ny >= 0 and nx < N and ny < N:
            if b[x][y] == b[nx][ny]:
                pass
            else:
                if b[x][y] == 1:
                    b[nx][ny] = 1
                else:
                    b[nx][ny] = 2
    return



for tc in range(1, T+1):
    N, M = map(int, input().split())

    b = [[0]*N for x in range(N)]

    for m in range(N//2 - 1, N//2 + 1):   # 오셀로 시작 전 준비
        for n in range(N//2 - 1, N//2 + 1):
            if m == n:
                b[m][n] = 2
            else:
                b[m][n] = 1

    print(b)

    for x in range(M):
        j, i, c = map(int, input().split())

        i = i-1
        j = j-1

        if c == 1:
            b[i][j] = 1
            check(i,j)

        else:
            b[i][j] = 2
            check(i,j)

    print(b)
