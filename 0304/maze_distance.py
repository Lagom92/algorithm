# 미로의 거리
T = int(input())

def f(i, j, n):
    if maze[i][j] == 3:
        return


for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for x in range(N)]

    si = 0
    sj = 0
    for j in range(N):
        if maze[N-1][j] == 2:
            si = N-1
            sj = j

    print(si, sj, N)
