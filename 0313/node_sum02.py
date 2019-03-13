# node 의 합_다른 아이디어(성공)
# import sys
# sys.stdin = open('input01.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for x in range(N)]

    num = N // 2
    total = 0
    s = 0

    for x in range(N):   # 정 가운데 가로의 합
        total += farm[num][x]

    for i in range(num):
        # print(farm[i][num-i:num+i+1])
        s += sum(farm[i][num-i:num+i+1])   # 위쪽 수들의 합
        # print("--")
        # print(farm[-i-1][num-i:num+i+1])
        s += sum(farm[-i-1][num-i:num+i+1])   # 아래쪽 수들의 합

    print('#{} {}'.format(tc, total+s))

