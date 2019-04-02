# 다익스트라

def dij(s, v):
    u = [s]
    for i in range(v+1):
        d[i] = adj[s][i]
    while len(u) != v:
        # u에 들어있지 않은 w중 d[w]가 최소인 w 찾기
        minV = 10000000
        w = 0
        for i in range(1, v+1):
            if i not in u:
                if d[i] < minV:
                    minV = d[i]
                    w = i
        u.append(w)
        for i in range(1, v+1):
            if adj[w][i] != 0 and adj[w][i] != 1000:    # 0 이나 max값이 아닌 것이면
                d[i] = min(d[i], d[w] + adj[w][i])

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[1000]*(V+1) for i in range(V+1)]
    for i in range(V+1):    # 대각선은 0으로 처리, 출발과 도착이 같은 경우 0
        adj[i][i] = 0

    for i in range(E):    # 인접 정보 추가
        n1, n2, w = map(int, input().split())    # w:가중치
        adj[n1][n2] = w

    # print(adj)
    s = 1    # 출발지는 1
    d = [0]*(V+1)

    dij(s, V)
    print(d)
    print(d[1:])