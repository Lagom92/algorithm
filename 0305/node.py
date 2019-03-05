# 노드의 거리
T = int(input())

def bfs(s, g, v):
    q = []   # 큐 생성
    visited = [0]*(v+1)   # visited 생성
    q.append(s)   # 시작점 인큐
    visited[s] = 1   # 시작점 방문표시

    while len(q) != 0:   # 큐가 비어있지 않으면
        n = q.pop(0)   # 디큐
        if n == g:   # 목적지 이면
            return visited[g]-1
        for i in range(1, v+1):   # 모든 노드 i에 대해
            # n에 인접이고 미방문이면
            if adj[n][i] != 0 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[n] + 1
    return 0


for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for i in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1   # 방향이 없는 그래프 이므로(무방향)
        adj[n2][n1] = 1

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, bfs(S, G, V)))