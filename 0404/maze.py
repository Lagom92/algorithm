T = int(input())

def f(i, j, s):
    global minV
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    if maze[i][j] == 3:
        if minV > s:
            minV = s
        return

    if s >= minV:
        return

    for k in range(4):
        nx = i + di[k]
        ny = j + dj[k]

        if 0 <= nx < N and 0 <= ny < N:
            if maze[nx][ny] != 1 and v[nx][ny] == 0:
                v[nx][ny] = 1
                f(nx, ny, s+1)
                v[nx][ny] = 0


for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for x in range(N)]

    minV = 10000000
    v = [[0]*(N+1) for x in range(N+1)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                f(i, j, -1)

    print(minV)