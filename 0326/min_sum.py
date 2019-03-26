# 최소 합
T = int(input())

def f(x,y,t):
    global minV, N
    if x == N-1 and y == N-1:   # goal 도착
        t += arr[N-1][N-1]
        if minV > t:
            minV = t
    elif x >= N or y >= N:   # 범위 넘어가면 끝
        return
    elif t >= minV:   # 검색중 합t 가 이미 최소값보다 커지면 끝
        return
    else:   # 오른쪽이나 아래로 탐색하면서 값 더해줌
        f(x+1, y, t + arr[x][y])
        f(x, y+1, t + arr[x][y])

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]

    minV = 10*N**2
    f(0, 0, 0)

    print('#{} {}'.format(tc, minV))
