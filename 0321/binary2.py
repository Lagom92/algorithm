# 이진수2

T = int(input())
for tc in range(1, T+1):
    N = input()
    res = ""
    num = float(N)
    cnt = 0

    while cnt < 13:
        cnt += 1
        num = num*2
        if num >= 1:
            res += "1"
            num -= 1
        else:
            res += "0"
        if num == 0:
            break
    if len(res) >= 13:
        res = "overflow"

    print('#{} {}'.format(tc, res))
