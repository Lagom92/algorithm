# 숫자 배열 회전
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for i in range(N)]

    # print(N)
    # print(arr)
    result = []

    for i in range(N):
        r90 = ""
        r180 = ""
        for j in range(N):
            r90 += arr[j][i]
            # r180 += arr[i][-j+N-1]

        print(r90)
        # print(r180)
        result.append(r90)
        # result.append(r180)


    print(result)


# 아 모르겠따