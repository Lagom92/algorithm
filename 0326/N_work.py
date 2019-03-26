# a,b,c 사람이 3개의 일을 각자 하나씩 할때 최소 값은 무엇인가??
# 순열 이용

T = int(input())

def npr(n, k):  # n이 순열의 길이, k는 숫자를 결정할 자리
    global minV
    if n == k:
        s = 0
        for j in range(len(arr)):
            s += arr[j][p[j] - 1]
            if minV < s:
                return
        if minV > s:
            minV = s
    else:
        for i in range(k, n):
            p[i], p[k] = p[k], p[i]
            npr(n, k + 1)
            p[i], p[k] = p[k], p[i]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for x in range(N)]

    # arr = [[13, 8, 10], [7, 10, 12], [12, 8, 10]]
    # p = [1, 2, 3]

    p = [x for x in range(1, N+1)]

    minV = 1000000
    npr(N, 0)

    print('#{} {}'.format(tc, minV))