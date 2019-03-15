# 승현이의 수학공부

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())

    cnt = 0
    num = 0

    while X > 0:
        n = X % 10
        X = X // 10
        num += n * (N**cnt)
        cnt += 1
    res = num % (N-1)

    print('#{} {}'.format(tc, res))

    # 사이트에 파이썬이 없음
    # input
    # 3
    # 9 234
    # 5 123
    # 3 102

    # output
    # #1 1
    # #2 2
    # #3 1