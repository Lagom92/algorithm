T = int(input())
for tc in range(1, T+1):
    color = list(map(int, input().split()))
    color2 = list(map(int, input().split()))
    print(color)
    cnt = 0
    arr = [[0]*10 for x in range(10)]
    for i in range(10):
        for j in range(10):
            if color[2] >= i >= color[0] and color[3] >= j >= color[1]:
                arr[i][j] += 1

    for i in range(10):
        for j in range(10):
            if color2[2] >= i >= color2[0] and color2[3] >= j >= color2[1]:
                arr[i][j] += 2
            if arr[i][j] == 3:
                cnt += 1
    print(arr)
    print(cnt)
