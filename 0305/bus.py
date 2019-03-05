# 삼성시의 버스 노선

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = [list(map(int, input().split())) for x in range(N)]
    P = int(input())

    box = []
    result = ""

    for i in range(N):
        for j in range(1):
            for k in range(line[i][0], line[i][1]+1):
                box.append(k)

    for m in range(1, P):

        result += str(box.count(m)) + " "
    print('#{} {}'.format(tc, result))

