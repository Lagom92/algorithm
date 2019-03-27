# 최소 생산 비용
# 시간 초과 발생함

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

    p = [x for x in range(1, N+1)]

    minV = 1000000
    npr(N, 0)

    print('#{} {}'.format(tc, minV))