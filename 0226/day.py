# 날짜 계산기
T = int(input())
for tc in range(1, T+1):
    M, D, m, d = map(int, input().split())

    calendar = {
        1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
        7:31, 8:31, 9:30, 10:31, 11:30, 12:31
    }
    n = m-M
    day = d - D +1

    if n > 0:
        for i in range(M, M+n):
            day += calendar[i]
    print(f"#{tc} {day}")