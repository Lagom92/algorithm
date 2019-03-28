# 최소 생산 비용
T = int(input())

def f(n, r, s):
    global minV
    if n == r:
        if s < minV:
            minV = s
    elif s >= minV:
        return
    else:
        for i in range(n):
            if visited[i] == 0:    # 사용한적 없으면
                visited[i] = 1
                f(n, r+1, s+costs[r][i])
                visited[i] = 0

for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for x in range(N)]
    visited = [0]*N
    minV = 100*N
    f(N, 0, 0)
    print('#{} {}'.format(tc, minV))