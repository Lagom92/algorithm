# 화물 도크
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for x in range(N)]

    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1])
    cnt = 0

    end = 0
    for i in range(N):
        if arr[i][0] >= end:
            end = arr[i][1]
            cnt += 1
    print('#{} {}'.format(tc, cnt))