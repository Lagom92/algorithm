# 점프_백
# 시간초과남
def f(i, j):
    k = board[i][j]
    if k == 0:
        v[i][j] += 1
        return
    if 0 <= i+k < N and 0 <= j < N:
        f(i+k, j)
    if 0 <= i < N and 0 <= j+k < N:
        f(i, j+k)

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
v = [[0]*N for _ in range(N)]
f(0, 0)
print(v[N-1][N-1])