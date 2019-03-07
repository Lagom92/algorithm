# 단지 번호 붙이기

n = int(input())
a = [list(input()) for x in range(n)]
cnt = 0
res = []

def f(x, y):
    global cnt
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    a[x][y] = '0'
    cnt += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if a[nx][ny] == '1':
            f(nx, ny)

for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt = 0
            f(i, j)
            res.append(cnt)

print(len(res))
print(res)
res.sort()
for i in res:
    print(i)
