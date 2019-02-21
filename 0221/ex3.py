# DFS
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(n, v):
    stack = []
    visited = [0]*(V+1)  # V번 노드까지 방문표시
    visited[n] = 1
    stack.append(n)
    while len(stack) != 0:  # 스택이 비어있지 않으면
        n = stack.pop()
        print(n, end=" ")
        for i in range(1, v+1):
            if adj[n][i] != 0 and visited[i] == 0:  # n 과 i 가 인접이고 방문하지 않은 노드면
                stack.append(i)
                visited[i] = 1


V, E = map(int, input().split())
edge = list(map(int, input().split()))

adj = [[0]*(V+1) for i in range(V+1)]

for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1  # 1 2 가 연결되있어,
    adj[n2][n1] = 1  # 2 1 도 연결되어있어, 화살표가 있으면 이건 없어야 함, 방향성이 없는 그래프

dfs(1, V)