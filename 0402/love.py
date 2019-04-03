# 망한거
T = int(input())


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]

    print(arr)
    res = []
    for i in range(N-1):
        for j in range(2):
            res.append(arr[i][j]-arr[i+1][j])
    print(res)
