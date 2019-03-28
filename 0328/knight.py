# 나이트의 이동_백
T = int(input())

def bfs(i, j):
    # global N, visited
    di = [2, 2, -2, -2, -1, 1, 1, -1]
    dj = [1, -1, 1, -1, 2, 2, -2, -2]
    q = []
    q.append(i)
    q.append(j)

    while q:
        x = q.pop(0)
        y = q.pop(0)

        if x == endI and y == endJ:
            return visited[x][y]

        for k in range(8):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append(nx)
                    q.append(ny)
    return 0

for tc in range(1, T+1):
    N = int(input())
    startI, startJ = map(int, input().split())
    endI, endJ = map(int, input().split())
    visited = [[0]*N for x in range(N)]

    res = bfs(startI, startJ)
    print(res)