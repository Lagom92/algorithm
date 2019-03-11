import sys
sys.stdin = open('input01.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    result = []
    N, M = map(int, input().split())
    for x in range(M):
        arr = list(map(int, input().split()))
        if len(result) == 0:
            result += arr

        else:
            if arr[0] > max(result):
                result = result + arr
            else:
                for i in range(len(result)):
                    if arr[0] < result[i]:
                        result = result[0:i] + arr + result[i:len(result)]
                        break

    print('#{}'.format(tc), end=" ")
    for j in range(10):
        print(result[-j-1], end=" ")
    print()

