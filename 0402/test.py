def Dij(s, v):
    u = [s]

    for i in range(v+1):
        d[i] = adj[s][i]

    while len(u) != v:
        minV = 10000000
        w = 0
        for i in range(1, v + 1):
            if i not in u:
                if d[i] < minV:
                    minV = d[i]
                    w = i

        u.append(w)

        for i in range(1, v+1):
            if adj[w][i] != 0 and adj[w][i] != 100000:    # 0 이나 max값이 아닌 것이면
                d[i] = min(d[i], d[w] + adj[w][i])



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[100000]*(V+1) for x in range(V+1)]     # 행렬만듬

    for i in range(V+1):    # 왼오 대각선 = 0, 출발 = 도착
        adj[i][i] = 0

    for i in range(E):    # 인접 정보 추가
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w

    s = 0
    d = [0]*(V+1)

    Dij(s, V)


    print(d)
    print(d[-1])