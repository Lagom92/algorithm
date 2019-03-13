# node 의 합_나(미완성본)
# import sys
# sys.stdin = open('input01.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for x in range(N)]

    num = N // 2
    total = 0
    s = 0
    # for i in range(num+1):
    #     for j in range(num+1):
    #         if i >= num - j-1:  # 오른쪽 아래 계단 모양
    #             print(farm[i][j])
    #             total += farm[i][j]
    # print("===")
    # for i in range(num+1):
    #     for j in range(num, N):
    #         if i + num >= j:  # 왼쪽 아래 계단 모양
    #             print(farm[i][j])
    #             total += farm[i][j]
    # print("===")
    #
    # for i in range(num, N):
    #     for j in range(num+1):
    #         if i <= j+num:  # 오른쪽 위 계단 모양
    #             print(farm[i][j])
    #             total += farm[i][j]
    #
    # print("===")
    for i in range(num,N):
        for j in range(num,N):
            if i-num >= N-num - j-1 :  # 왼쪽 위 모음

                print(farm[i][j])

    print("===")

    # for m in range(N):   # 전체에서 가로 세로 십자모양
    #     for n in range(N):
    #         if m == num or n == num:
    #             print(farm[m][n])
    #             s += farm[m][n]
    # print("===")

    # 정 가운데 가로 세로가 중복이므로 결과에서 제거해야함

    print('#{} {}'.format(tc, total-s))