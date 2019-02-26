# 시각덧셈
T = int(input())
for tc in range(1,T+1):
    H, M, h, m = map(int, input().split())

    print(tc)
    print(H, M, h, m)

    resultH = 0
    resultM = 0

    resultH = H + h
    resultM = M + m

    if resultH > 12:
        resultH = resultH - 12
    elif resultM >= 60:
        resultM = resultM - 60
        resultH = resultH + 1

    print(f"#{tc} {resultH} {resultM}")