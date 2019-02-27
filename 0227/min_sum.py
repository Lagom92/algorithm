# 배열 최소 합
from itertools import permutations
import sys
sys.stdin = open('input03.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]

    print(N)
    print(arr)

    for i in permutations(range(N)):
        # print(j)
        for j in range(N):
            print(arr[i[j]])
