# 보급로
# 남에꺼
import sys
sys.stdin = open('input03.txt','r')

def bfs(i, j):
    di = [0, 1, 0, -1]    # 4방향 탐색
    dj = [1, 0, -1, 0]

    visited[i][j] = 1    # 방문표시
    q = []
    q.append(i)
    q.append(j)

    while q:
        x = q.pop(0)
        y = q.pop(0)

        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if 0 <= dx < N and 0 <= dy < N:
                if visited[dx][dy] == 0 or dp[dx][dy] > dp[x][y] + arr[dx][dy]:    # 방문하지 않았거나,  ...?
                    visited[dx][dy] = 1
                    q.append(dx)
                    q.append(dy)
                    dp[dx][dy] = dp[x][y] + arr[dx][dy]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for i in range(N)]

    visited = [[0] * N for i in range(N)]
    dp = [[0] * N for i in range(N)]

    bfs(0, 0)
    print("#{} {}".format(t, dp[-1][-1]))