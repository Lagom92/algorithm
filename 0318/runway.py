# 활주로
import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    zone = [list(map(int, input().split())) for tc in range(N)]

    print(N, X)
    print(zone)

    cnt = 0
    for i in range(N):
        flag = 0
        c = 0
        f = 0
        for j in range(N-1):
            if zone[i][j] == zone[i][j + 1]:
                a = zone[i][j]
                if zone[i].count(a) == N:
                    cnt += 1

            if zone[i][j] - zone[i][j+1] == 1:
                flag = 1

            if flag == 1 and zone[i][j] == zone[i][j+1]:
                c += 1

            if zone[i][j] - zone[i][j+1] == -1:
                flag = 0

        print(c)
        if c < X:
            cnt += 1
    print(cnt)



