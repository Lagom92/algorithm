# 연습문제2
# 합이 50인 부분집합 구하기_p206


def f(n, k, s, rs):
    global cnt
    cnt += 1
    if s == 50:
        for i in range(k):
            if b[i] == 1:
                print(a[i], end=" ")
        print()
    elif s > 50:    # 백트레킹_합이 50이 넘어버리면 더이상 진행을 안하게함
        return
    elif s + rs < 50:
        return
    elif n == k:
        return
    else:
        b[n] = 1    # a[n]이 부분집합에 포함되는 경우
        f(n+1, k, s+a[n], rs-a[n])
        b[n] = 0    # a[n]이 부분집합에 포함되지 않는 경우
        f(n+1, k, s, rs-a[n])


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [0]*len(a)
cnt = 0
f(0, len(a), 0, sum(a))
print('cnt: {}'.format(cnt))