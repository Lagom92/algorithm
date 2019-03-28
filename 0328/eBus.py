# 전기버스2

T = int(input())
def f(n, k, e, c):    # 현재 n, 종점 k, 남은 에너지 e, 교환횟수 c
    global minC
    if n == k:    # 종점에 도착하는 경우
        if minC > c:
            minC = c
    elif c > minC:
        return
    else:    # 통과, 교체
        if e > 0:    # 통과
            f(n+1, k, e-1, c)
        f(n+1, k, M[n]-1, c+1)    # 교체

for tc in range(1, T+1):
    a = list(map(int, input().split()))
    N = a[0]    # 정류장의 수 N
    M = a[1:N]    # 배터리 용량들 M

    minC = 1000
    f(0, N-1, 0, 0)
    print('#{} {}'.format(tc, minC-1))