T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    u = [0]*N    # 받은 투표 모음

    for i in range(M):
        for j in range(N):
            if B[i] >= A[j]:
                u[j] += 1
                break
    # print(u)
    res = max(u)
    print('#{} {}'.format(tc, u.index(res)+1))