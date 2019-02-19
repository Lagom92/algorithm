import sys
sys.stdin = open('input02.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    print(test_case, N, arr)
    R = []
    B = []
    field = [[0]*10 for i in range(10)]
    P = 0



