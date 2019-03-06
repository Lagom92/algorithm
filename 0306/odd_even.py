# 홀수일까 짝수일까

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = ""
    if N % 2 ==1:
        result = "Odd"
    else:
        result = "Even"

    print('#{} {}'.format(tc, result))
