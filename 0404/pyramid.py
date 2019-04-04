T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    N = 100
    arr = [[0]*N for x in range(N)]


    n = 5
    k = 3
    cnt = 0
    c = [n-k-1, n-k, n-k+1, n-1, n+1, n+k, n+k+1, n+k+2]

