# 1,2,3 더하기_백
import sys
input = sys.stdin.readline
def f(n):
    if memo[n] != 0:
        return memo[n]
    elif n <= 2:
        return n
    elif n == 3:
        return 4
    else:
        memo[n] = (f(n-1) + f(n-2) + f(n-3))%1000000009
        return memo[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    memo = [0] * 10000002
    res = f(N)
    print(res)