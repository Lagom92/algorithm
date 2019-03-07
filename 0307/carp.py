# 붕어빵_쌤

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(M)]

    box = [0]*61
    print(box)
    for i in range(M):
        box[arr[i][0]] = int(-arr[i][1])

    print(box)

    for j in range(1, 60):
        box[j] = N + box[j] + box[j-1]

    print(box)
    print(len(box))
