# 수도 요금 경쟁
T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = list(map(int, input().split()))

    Awon = P*W
    Bwon = Q if W <= R else Q + (W-R)*S

    result = Bwon if Awon > Bwon else Awon

    print(f"#{tc} {result}")
