# 파리 퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().split() for x in range(N)]

    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for m in range(M):
                for n in range(M):
                    total += int(arr[i+m][j+n])
            if total > maxV:
                maxV = total
    print('#{} {}'.format(tc, maxV))
