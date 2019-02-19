# 금속 막대 문제
import sys
sys.stdin = open('input05.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(N)
    print(arr)
    result = []
    for i in range(len(arr)):
        if i%2==0:
             a = arr[i],arr[i+1]
             result.append(a)
    print(result)
    for j in result:
        result[0]

