import sys
sys.stdin= open('input02.txt', 'r')

def f(i, j, n):
    stack = [i, j]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 1
    while stack:
        si = stack.pop(0)
        sj = stack.pop(0)
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < n and 0 <= nj < n and (arr[si][sj] + 1) == arr[ni][nj]:
                stack.append(ni)
                stack.append(nj)
                cnt += 1
    return cnt


for t in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    res_list = [0] * ((N ** 2) + 1)
    for i in range(N):
        for j in range(N):
            res_list[arr[i][j]] = f(i, j, N)
    res_max = max(res_list)
    res = res_list.index(res_max)
    print('#{} {} {}'.format(t + 1, res, res_max))