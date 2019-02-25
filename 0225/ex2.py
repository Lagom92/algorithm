# 중복순열
# 1,2,3,4,5 중 3개의 숫자를 중복 사용해 3자리 숫자 만들기
def f(n, k, m):
    global cnt
    if n == k:
        print(p)
        cnt += 1
        return
    else:
        for i in range(1, m+1):  # 사용하는 숫자의 개수
            p[n] = i
            f(n+1, k, m)

k = 3
m = 5
p = [0] * k
cnt = 0
f(0, k, m)
print(f"cnt: {cnt}")