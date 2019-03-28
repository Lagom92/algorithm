# 최소 생산 비용
# 순열
T = int(input())

def f(n, r, s):   # 전체 상품의 수 n, r번 상품의 공장 결정, r-1번 상품까지의 생산 비용
    global minV
    if n == r:    # 모든 상품에 대해 결정이 되면
        if s < minV:
            minV = s
    elif s >= minV:    # 백트래킹
        return
    else:     # 생산지 결정, 아직 상품이 결정되지 않은 공장에 대해
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