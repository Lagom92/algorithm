# 중복 순열(1,2,3 을 중복사용해서 3자리 숫자 만들기)
def f(n, k):
    global cnt
    if n == k:
        print(p)
        cnt += 1
        return
    else:
        for i in range(1, k+1):
            p[n] = i
            f(n+1, k)

k = 3
p = [0] * k
cnt = 0
f(0, k)
print(f"cnt: {cnt}")