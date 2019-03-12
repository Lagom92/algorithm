import sys
sys.stdin = open('input02.txt','r')

T = int(input())

def f(x, y):
    global cnt
    cnt += 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and ny >= 0 and nx < N and ny < N:
            if rooms[nx][ny] == rooms[x][y] + 1:
                f(nx, ny)
    return

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for x in range(N)]

    cnt = 0
    minV = N * N
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            f(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                minV = rooms[i][j]
            if max_cnt == cnt and rooms[i][j] < minV:
                minV = rooms[i][j]

    print('#{} {} {}'.format(tc, minV, max_cnt))