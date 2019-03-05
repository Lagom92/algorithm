# 미로의 거리

def bfs(i, j, n):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = []   # 큐 생성
    visited = [[0]*n for i in range(N)]
    q.append(i)   # 시작점 인큐
    q.append(j)
    visited[i][j] = 1   # 시작점 방문 표시

    while len(q) != 0:   # 큐가 비어있지 않으면 반복
        i = q.pop(0)   # 디큐
        j = q.pop(0)
        if maze[i][j] == 3:   # 디큐한 칸 처리, 목적지 인지 확인하는 과정
            return visited[i][j]-2
        for k in range(4):   # 인접한 4방향에 대해
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and nj >= 0 and ni < n and nj < n:  # 미로를 벗어나지 않으면
                # 벽이 아니고 방문하지 않은 칸이면 인큐
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append(ni)
                    q.append(nj)
                    visited[ni][nj] = visited[i][j] + 1
    return 0   # 목적지에 통과하지 못하는 경우


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [[int(x) for x in input()] for i in range(N)]
    for i in range(N):
        if 2 in maze[i]:
            sRow = i   # 출발 row index
            sCol = maze[i].index(2)   # 출발 column index
    print('#{} {}'.format(tc, bfs(sRow, sCol, N)))