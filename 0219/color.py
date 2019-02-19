# 색칠하기
import sys
sys.stdin = open('input02.txt', 'r')

T=int(input())
for tc in range(1,T+1):
    b = [[0] * 10 for i in range(10)]  # 10*10 격자
    N = int(input())  #영역의 개수
    count = 0

    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        row = r2-r1+1
        col = c2-c1+1
        for i in range(row):
            for j in range(col):
                b[i+r1][j+c1] += color
                if b[i+r1][j+c1] == 3:
                    count += 1

    print(f"#{tc} {count}")

