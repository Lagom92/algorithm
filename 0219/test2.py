T = int(input())
for tc in range(1, T+1):
    time = list(map(int, input().split()))

    h = 0
    m = 0

    h = time[0] + time[2]
    m = time[1] + time[3]

    if m >= 60:
        m -= 60
        h += 1

    if h > 12:
        h -= 12

    print(f"#{tc} {h} {m}")
