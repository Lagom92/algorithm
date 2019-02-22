# 회문2
import sys
sys.stdin = open('input.txt', 'r')

def pal(N, M, string):
    for i in range(N):  # 0 -> N-1 까지
        for j in range(N - M + 1):  # 0 -> N-M 까지
            a = ""
            b = ""
            a = "".join(string[i])[j:j + M]
            if a == a[::-1]:  # 회문 이면
                return a
            for k in range(M):
                b += "".join(string[j + k])[i]
            if b == b[::-1]:  # 회문이면
                return b

for test_case in range(10):
    tc = int(input())
    arr = [list(input().split()) for i in range(100)]

    max_cnt = 0
    result = ""
    for i in range(100, -1, -1):
        a = pal(100, i, arr)
        if a != None:
            result = a
            break

    print(f"#{tc} {len(result)}")




