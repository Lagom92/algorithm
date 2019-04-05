def f(n, N, K):
    global cnt
    if n == N:
        s = 0
        for i in range(N):
            if b[i] == 1:
                s += a[i]
        if s == K:
            cnt += 1
            for i in range(N):
                if b[i] == 1:
                    print(a[i], end=" ")
            print()
        return
    else:
        b[n] = 0
        f(n+1, N, K)
        b[n] = 1
        f(n+1, N, K)

# T = int(input())
T = 1
for tc in range(1, T+1):
    # N, K = map(int, input().split())
    # a = list(map(int, input().split()))

    N, K = 4, 3
    a = [1, 2, 1, 2]

    b = [0]*N # 원소의 포함여부를 나타내는 배열
    cnt = 0
    f(0, N, K)
    print('#{} {}'.format(tc, cnt))

    # 1 2
    # 2 1
    # 1 2
    # 1 2
    # 1 4