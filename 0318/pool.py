# 수영장
T = int(input())

def f(n, s):
    global year, minV, cnt

    if n >= 12:
        s = mon*cnt
        minV.append(s)
        return
    else:
        s = plan[n] * day + s
        f(n+1, s)

        if plan[n] > 0:
            cnt += 1

            f(n+3,s)

        else:
            cnt = 0



for tc in range(1, T+1):
    day, mon, mon3, year = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    print(day, mon, mon3, year)
    print(plan)
    minV = []
    minV.append(year)
    cnt = 0
    f(0,0)
    print(minV)