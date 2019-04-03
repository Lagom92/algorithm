# 공통 단어 검색
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        A.append(input())
    for j in range(M):
        B.append(input())

    cnt = 0
    for i in A:
        if i in B:
            cnt += 1

    print('#{} {}'.format(tc, cnt))