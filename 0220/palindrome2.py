import sys
sys.stdin = open('input06.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    words = [list(input().split()) for i in range(N)]

    print(N)
    print(M)
    print(words)
    result = ""

    for i in range(N-1):
        for j in range(N-1):
            result += words[N][N]

    print(result)

# 에러나옴 나중에 수정