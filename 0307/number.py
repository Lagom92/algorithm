# 최빈수 구하기
# import sys
# sys.stdin = open('input02.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    grade = list(input().split())
    grade.sort(reverse=True)

    result = 0
    maxcnt = 0
    for i in grade:
        cnt = grade.count(i)
        if cnt > maxcnt:
            maxcnt = cnt
            result = i
    # print(f"#{tc} {result}")
    print('#{} {}'.format(tc, result))