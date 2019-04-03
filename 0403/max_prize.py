import sys
sys.stdin = open('input02.txt', 'r')

def swap(num, c):
    global res, maxV
    if c == cnt:
        if num > maxV:
            maxV = num
        return
    if c == 7:
        if (cnt-7) % 2 == 1:
            c = cnt - 1
        else:
            c = cnt

    number = list(str(num))
    N = len(number)
    for i in range(0, N-1):
        for j in range(i+1, N):
            if number[i] <= number[j]:
                number[i], number[j] = number[j], number[i]
                a = int(''.join(number))
                swap(a, c + 1)
                # number[i], number[j] = number[j], number[i]
                number = list(str(num))

T = int(input())
for tc in range(1, T+1):
    num, cnt = map(int, input().split())
    res = []
    maxV = 0
    result = []
    swap(num, 0)
    result.append(maxV)
    print('#{} {}'.format(tc, maxV))
