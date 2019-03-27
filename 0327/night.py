# 나이트의 이동_백7562
# 공부 ㄱㄱㄱ

T = int(input())

def f(x, y, c):
    global N, e1, e2
    arr[x][y] = 1
    dx = [2, 2, 1, -1, -2, -2, 1, -1]
    dy = [1, -1, -2, -2, 1, -1, 2, 2]

    if x == e1 and y == e2:
        print(c)
        return

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 0:
                f(nx, ny, c+1)


for tc in range(1, T+1):
    N = int(input())
    s1, s2 = list(map(int, input().split()))
    e1, e2 = list(map(int, input().split()))
    arr = [[0]*N for x in range(N)]
    f(s1, s2, 0)


