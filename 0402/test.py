def f(n, k, s):
    global minV
    if n == k:
        if minV > s:
            minV = s
    elif s >= minV:
        return
    else:
        for i in range(n):
            if u[i] == 0:
                u[i] = 1
                f(n, k+1, s+ adj[k][i])
                u[i] = 0
