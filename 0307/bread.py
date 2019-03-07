T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    cnt = 0
    if A > B:
        A, B = B, A
    if C > A:
        while C >= A:
            C = C - A
            cnt += 1
    print('#{} {}'.format(tc, cnt))
