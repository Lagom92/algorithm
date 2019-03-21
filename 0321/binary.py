# 이진수
# 파이선의 함수들을 이용한것

T = int(input())
for tc in range(1, T+1):
    N, num16 = input().split()
    a = int(num16,16)
    res = bin(a)[2:]
    while len(res) < len(num16)*4:
        res = '0' + res
    print('#{} {}'.format(tc, res))