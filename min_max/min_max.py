import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    maxV = A[0]
    minV = A[0]
    for i in range(0, N):
        maxV = A[i] if maxV < A[i] else maxV
    for i in range(0, N):
        minV = A[i] if minV > A[i] else minV
    print(f"#{test_case} {maxV-minV}")

