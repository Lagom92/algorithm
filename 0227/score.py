# 조교의 성적 매기기
import sys
sys.stdin = open('input05_sample.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]

    print(N, K)
    print(arr)

    total = []
    for i in range(N):
        print(arr[i][0],arr[i][1],arr[i][2])
        a = arr[i][0]*0.35 + arr[i][0]*0.45 + arr[i][0]*0.20
        total.append(a)
    print(total)