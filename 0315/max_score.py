# 최대 성적표 만들기
import sys
sys.stdin = open('input02.txt','r')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    maxV = 0
    score.sort()
    for i in range(K):
        maxV += score[-i-1]
    print('#{} {}'.format(tc, maxV))
