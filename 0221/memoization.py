# Memoization
# 피보나치

def f(n):
    if n>= 2 and memo[n] == 0:
        memo[n] = f(n-1) + f(n-2)
    return memo[n]

N = 5
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1

print(f(N))
print(memo)