# 숫자 교환 연습하기_2(최대 상금)
# input
# 3
# 123 1
# 2737 1
# 32888 2

# 최대 상금 _ 쌤
# import sys
# sys.stdin = open('input01.txt', 'r')

def f(n, k, c):
    global total, minC
    if n == k or c == 0:
        # if c == 0:   # 주어진 횟수 만큼 교환한 결과
            # print(card)
        a = ''.join(card)
        if total < int(a):
            total = int(a)
            if minC > c:
                minC = c
        return
    else:
        for i in range(0, k):
            card[n], card[i] = card[i], card[n]
            # print(card)
            if i == n:   # 자기 자신과 교환이므로, 실제로는 교환하지 않는 경우
                f(n+1, k, c)
            f(n+1, k, c-1)   # 교환하는 경우로 교환 횟수 -1
            card[n], card[i] = card[i], card[n]

T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()
    total = 0
    minC = int(cnt)
    # print(num)   # 123
    # print(cnt)

    card = list(num)
    # print(card)   # ['1', '2', '3']

    f(0, len(card), int(cnt))
    # print(minC)
    result = str(total)
    # print(result)
    if minC % 2 == 1:
        a = result[-1]
        b = result[-2]
        result = result[0:len(card)-2] + a + b

    print('#{} {}'.format(tc, result))

