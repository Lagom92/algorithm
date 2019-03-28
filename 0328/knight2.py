# 나이트의 이동_백7562
# 공부 ㄱㄱㄱ

T = int(input())

def f(x, y):
    global N, e1, e2

    dx = [2, 2, 1, -1, -2, -2, 1, -1]
    dy = [1, -1, -2, -2, 1, -1, 2, 2]

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if nx == e1 and ny == e2:
                print(arr[nx][ny])
                return arr[nx][ny]

            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                f(nx, ny)


for tc in range(1, T+1):
    N = int(input())
    s1, s2 = list(map(int, input().split()))
    e1, e2 = list(map(int, input().split()))
    arr = [[0]*N for x in range(N)]
    res = f(s1, s2)
    print(res)
    f(s1, s2)