# 등산로 조성
T = int(input())

def f(x, y):
    global cnt
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    cnt += 1
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and table[x][y] > table[nx][ny]:
                f(nx, ny)
    return



for tc in range(1, T+1):
    N, K = map(int, input().split())
    table = [list(map(int, input().split())) for x in range(N)]
    print(tc)
    print(N,K)
    print(table)
    maxV = max(max(table))
    visited = [[0]*N for _ in range(N)]
    print(maxV)
    cnt = 0
    print("--")
    for i in range(N):
        for j in range(N):
            if table[i][j] == maxV:
                cnt = 0
                f(i,j)
                print(cnt)



