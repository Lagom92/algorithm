T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for x in range(N)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            for m in range(M):
                for n in range(M):
                    print(arr[i+m][j+n])

