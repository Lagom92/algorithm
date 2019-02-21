# 단순 2진 암호코드

import sys
sys.stdin = open('input01.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input())]

    print(arr)