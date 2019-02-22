# 회문
import sys
sys.stdin = open('input06_sample.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))   # M 회문의 길이,
    words = [input() for i in range(N)]  # N*N




    for i in range(N): # 가로 검사
        s=""
        for j in range(N-M):
                s += words[i][j]

        a = words[i]
        ar = a[::-1]
        if words[i] == ar:
            print(f"#{tc} {a}")

        else:   # 세로 검사
            b = ""
            for k in range(N):
                b += words[k][i]
            br = b[::-1]
            if b == br:
                print(f"#{tc} {b}")


