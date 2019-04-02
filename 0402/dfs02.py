# dfs 를 공부해보자 - 2
# 재귀 이용

def dfs(n, v):
    visited[n] = 1    # 방문표시
    print(n, end= " ")
    for i in range(1, v+1):
        if adj[n][i] != 0 and visited[i] == 0:
            dfs(i, v)

V, E = map(int, input().split())
edge = list(map(int, input().split()))

adj = [[0]*(V+1) for i in range(V+1)]

for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1
    visited = [0]*(V+1)

dfs(1, V)    # 1 부터 V까지