# 전기 카트
T = int(input())

def perm(n, k):   # 순열 만들기
    if k == n:
        res.append([1] + p + [1])   # 순열 앞뒤로 사무실 추가
    else:
        for i in range(k, n):
            p[i], p[k] = p[k], p[i]
            perm(n, k+1)
            p[i], p[k] = p[k], p[i]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [x for x in range(2, N+1)]
    res = []
    perm(N-1, 0)
    minV = 1000000

    for i in range(N-1):
        s = 0
        for j in range(N):
            a, b = res[i][j], res[i][j+1]
            s += arr[a-1][b-1]
            if s > minV:
                break
        if minV > s:   # 합 s 중 최소 찾기
            minV = s
    print('#{} {}'.format(tc, s))


