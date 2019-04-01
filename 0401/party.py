# 상원이의 생일파티
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(M)]

    cnt = 0
    r = []    # 초대장 받은 사람
    arr.sort(key=lambda i:i[1])

    for i in range(M):   # 상권이가 친한 친구 수
        if arr[i][0] == 1:
            r.append(arr[i][1])

    for j in range(len(r)):    # 친구의 친구 수, 양방향
        for k in range(M):
            if arr[k][0] == r[j]:
                if arr[k][1] not in r:
                    r.append(arr[k][1])
            if arr[k][1] == r[j]:
                if arr[k][0] not in r:
                    r.append(arr[k][0])

    # print(r)
    res = len(r)
    if 1 in r:
        res -= 1

    print('#{} {}'.format(tc, res))