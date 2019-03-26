# 최소 합
# ????
T = int(input())

def f(x, y):
    global box, res
    dx = [0, 1]
    dy = [1, 0]
    res.append(arr[x][y])
    # print(res)
    if x == N-1 and y == N-1:
        print(res)

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            f(nx, ny)

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]
    res = []
    t = 0
    f(0,0)