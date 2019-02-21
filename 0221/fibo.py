# 피보나치 수열 - 재귀함수 이용
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(10):
    print(fibo(i))

# 단점: 중복 호출이 많이 발생함