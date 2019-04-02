T = int(input())

for tc in range(1, T+1):
    res = 0
    L, R = map(int, input().split())

    for i in range(L, R+1):     # 약수 구하기
        for j in range(1, i + 1):
            if i % j == 0:
                # print(i, end=" ")
                if j % 2 == 1:    # 약수 중에서 홀수인것들 구하기
                    # print(j, end=" ")
                    res += j

    print('#{} {}'.format(tc, res))