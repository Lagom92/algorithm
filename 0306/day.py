# 날짜 계산기


T = int(input())
calendar = {
    '1': 31, '2': 28, '3': 31, '4': 30,
    '5': 31, '6': 30, '7': 31, '8': 31,
    '9': 30, '10': 31, '11': 30, '12': 31
    }

for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())

    day = 0

    for i in range(m1, m2):   # 월 계산
        day += calendar[str(i)]

    day += d2 - d1 +1   # 일 계산

    print('#{} {}'.format(tc, day))



