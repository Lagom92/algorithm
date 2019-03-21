# 이진수
T = int(input())
for tc in range(1, T+1):
    N, num16 = input().split()
    num10 = 0
    n = len(num16)
    for j in range(n):
        a = 0
        if num16[j] == 'A':
            a = 10
        elif num16[j] == 'B':
            a = 11
        elif num16[j] == 'C':
            a = 12
        elif num16[j] == 'D':
            a = 13
        elif num16[j] == 'E':
            a = 14
        elif num16[j] == 'F':
            a = 15
        else:
            a = int(num16[j])
        num10 += a * 16**(n-j-1)

    print('#{} '.format(tc), end="")
    for i in range(len(num16)*4-1, -1, -1):
        if num10 & (1 << i) == 0:
            print(0, end="")
        else:
            print(1, end="")
    print()