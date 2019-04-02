T = int(input())

def f(i, j):
    global res, num
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = []
    q.append(i)
    q.append(j)

    while q:

        y = q.pop(-1)
        x = q.pop(-1)

        num += str(grid[x][y])

        if len(num) == 7:
            if num not in res:
                res.append(num)
            num = ""


        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append(nx)
                q.append(ny)
    return



for tc in range(1, T+1):
    grid = [list(map(int, input().split())) for x in range(4)]

    res = []
    cnt = 0
    num = ""
    for i in range(4):
        for j in range(4):
            f(i, j)



    print(res)
    print(len(res))