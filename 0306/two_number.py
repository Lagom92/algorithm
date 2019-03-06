# 두 개의 숫자열
import sys
sys.stdin = open('input03.txt','r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    maxV = 0
    a = []
    if N > M:
        B, A = A, B
        M, N = N, M

    for k in range(M-N+1):
        result = []
        for i in range(N):
            result.append(A[i]*B[i+k])
        a.append(sum(result))

    print('#{} {}'.format(tc, max(a)))
