# 회문
# 나중에 더 공부
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())   # N*N, 길이가 M인 회문
    string = [input().split() for i in range(N)]   # N*N 글자판
    result = ""

    # while result == "":   # result 에 값이 있으면 while 끝남
    for i in range(N):   # 0 -> N-1 까지
        for j in range(N - M + 1):   # 0 -> N-M 까지
            a = ""
            b = ""
            a = "".join(string[i])[j:j + M]  # join(리스트를 문자열로)
            if a == a[::-1]:   # 회문 이면
                result = a
            for k in range(M):
                b += "".join(string[j + k])[i]
            if b == b[::-1]:  # 회문이면
                result = b
    print(f"#{tc} {result}")