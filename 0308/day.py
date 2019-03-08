# 2016 요일 맞추기
# 쌤

day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dsum = [0]*13 #전달까지 날짜의 합
for i in range (1, 13):
    dsum[i] = dsum[i-1]+day[i-1]

T = int(input())
for tc in range(1, T+1):
    m, d= map(int, input().split())
    print('#{} {}'.format(tc, (dsum[m]+d+3)%7))