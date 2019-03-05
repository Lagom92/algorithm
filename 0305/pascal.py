T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print('#{}'.format(tc))
    for m in range(N):
        for n in range(N):
            if arr[m][n] != 0:
                print(arr[m][n], end=" ")
        print()