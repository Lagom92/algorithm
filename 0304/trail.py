# 등산로 조성_3번규칙제거 버전

def f(i, j, c, n):   # i, j 좌표 , c: 지나온 칸 수, n: 크기
    global maxV
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    if maxV < c+1:
        maxV = c+1
    for k in range(4):   # 탐색할 방향
        ni = i + di[k]
        nj = i + dj[k]
        if ni > 0 and nj > 0  and ni < n and nj < n:   # 영역을 벗어나지 않고
            if h[i][j] > h[ni][nj]:   # 더 낮은 곳으로 이동
                f(ni, nj, c+1, n)


T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))

    h = [list(map(int, input().split())) for x in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(N):
            f(i, j, 0, N)
    print('#{} {}'.format(tc, maxV))