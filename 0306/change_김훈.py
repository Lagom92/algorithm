# 쉬운 거스름돈
import sys
sys.stdin = open('input02.txt','r')

T = int(input())
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T + 1):
    N = int(input())
    print("#{}".format(tc))
    for i in money_list:
        print(N // i, end=" ")
        N -= i * (N // i)
    print()