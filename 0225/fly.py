# 파리퇴치
import sys
sys.stdin = open('input02_sample.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]

    print(tc)
    print(N, M)
    print(arr)

    for i in range(N-M):
        result = 0
        for j in range(N-M):
            result += arr[i][j]
            print(result)