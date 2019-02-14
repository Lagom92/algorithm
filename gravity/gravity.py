import sys
sys.stdin = open('input.txt', 'r')

arr = list(map(int, input().split()))
for i in range(len(arr)):
    print(arr[i], end=' ')