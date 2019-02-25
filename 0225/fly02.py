# 기차 사이의 파리
T =int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    print(f"#{tc} {D / (A + B)*F}")