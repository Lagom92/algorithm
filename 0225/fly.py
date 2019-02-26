# 파리퇴치
import sys
sys.stdin = open('input02.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    maxV=0
    for i in range(N-M+1):  # 가로 N-M 개
        for j in range(N-M+1):  # 세로 N-M 개
            result = 0
            for k in range(i, i+M):  # 가로 M 개
                for l in range(j, j+M):  # 세로 M 개
                    result += arr[k][l]
            if maxV < result:  # 최대값 구하기
                maxV = result
    print(f"#{tc} {maxV}")