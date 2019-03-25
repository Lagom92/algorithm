# 신입사원_백

import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for x in range(N)]

    a.sort(key=lambda x:x[0])
    print(a)
    # a.sort(key=lambda x:x[1])
    # print(a)

    m = []
    limit = a[0][1]
    for i in range(1, N):
        if a[i][1] > limit:
            m.append(a[i])
    print(m)
    print(len(a) - len(m))
