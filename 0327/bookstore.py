# 장훈이의 높은 선반
T = int(input())
def f(n, k, s):
    global B
    if s >= B:
        res.append(s)
    if n == k:
        return
    else:
        b[n] = 1
        f(n+1, k, s+H[n])
        b[n] = 0
        f(n+1, k, s)

for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    b = [0]*N
    res = []

    f(0, len(H), 0)

    print('#{} {}'.format(tc, min(res)-B))