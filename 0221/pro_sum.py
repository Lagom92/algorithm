# professional 합

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # print(N)
    # print(arr)
    num = 0
    maxV = 0

    for i in range(1, 2**N):

        for j in range(N):


            
# 부분 집합을 구해서 각각의 합을 구한 후 그 최대 값 비교
            
