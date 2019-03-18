T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    res = A.replace(B,"-")
    print('#{} {}'.format(tc, len(res)))
