import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    top = num[0]
    bottom = 10000000
    for i in range(0, N-M+1):
        a = 0
        for j in range(i, i+M):
            a += num[j]
        if top < a:
            top = a
        if bottom > a:
            bottom = a

    print(f"#{test_case} {top-bottom}")