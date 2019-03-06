def makarr(x, y):
    arr = []
    for i in range(y):
        arr.append([0]*x)
    count = 1
    a_wall = 0
    b_wall = x-1
    c_wall = y-1
    d_wall = 0

    while a_wall <= c_wall or b_wall >= d_wall and count != x*y:
        for i in range(d_wall, b_wall):
            if count > x*y:
                break
            arr[d_wall][i] = count
            count += 1

        for i in range(a_wall, c_wall):
            if count > x*y:
                break
            arr[i][b_wall] = count
            count += 1

        for i in range(b_wall, d_wall, -1):
            if count > x*y:
                break
            arr[c_wall][i] = count
            count += 1

        for i in range(c_wall, a_wall, -1):
            if count > x*y:
                break
            arr[i][d_wall] = count
            count += 1

        if a_wall == b_wall == c_wall == d_wall:
            arr[d_wall][b_wall] = count

        a_wall += 1
        b_wall -= 1
        c_wall -= 1
        d_wall += 1

    for i in range(x):
        for j in range(y):
            print(arr[i][j], end=" ")
        print()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    makarr(N,N)