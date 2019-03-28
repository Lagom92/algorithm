T = int(input())

def f(i, j):
    di = [2, 2, -2, -2, 1, -1, 1, -1]
    dj = [1, -1, 1, -1, 2, 2, -2, -2]
    q = []
    q.append(i)
    q.append(j)

    while q:
        x = q.pop(0)
        y = q.pop(0)
        if x == e1 and y == e2:
            return v[x][y]

        for k in range(8):
            nx = x + di[k]
            ny = y + dj[k]

            if 0 <= nx < N and 0 <= ny < N:
                if v[nx][ny] == 0:
                    v[nx][ny] = v[x][y] + 1
                    q.append(nx)
                    q.append(ny)
    return 0

for tc in range(1, T+1):
    N = int(input())
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    v = [[0]*N for x in range(N)]
    res = f(s1,s2)
    print(res)