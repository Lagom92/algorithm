# 동철이의 일 분배
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

def f(n, r, s):
    global maxV
    if n == r:
        if s > maxV:
            maxV = s
        return
    elif s <= maxV:
        return
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                f(n, r+1, s*table[r][i])    # r번 사람이 i번 일을할때 성공확률을 s에 곱함
                used[i] = 0

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for x in range(N)]
    used = [0]*N
    maxV = 0

    for i in range(N):
        for j in range(N):
            table[i][j] *= 0.01
    # print(table)

    f(N, 0, 1)
    res = maxV * 100
    result = "%0.6f" %res    # 소수점 6번째 까지 출력

    print('#{} {}'.format(tc, result))