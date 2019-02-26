# 그래프 경로
import sys
sys.stdin = open('input03.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    V, E = input().split()
    arr = [list(map(int, input().split())) for x in range(int(E))]
    S, G = input().split()

