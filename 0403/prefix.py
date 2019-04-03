T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = []
    B = []
    for x in range(N):
        A.append(input())
    for x in range(M):
        B.append(input())

    res = []
    cnt = 0
    for i in range(M):
        for j in range(N):
            a = A[j]
            if B[i] == a[:len(B[i])]:
                if B[i] not in res:
                    res.append(B[i])
                    cnt += 1

    print('#{} {}'.format(tc, cnt))