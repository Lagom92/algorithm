# 최빈수 구하기
import sys
sys.stdin = open('sample_input02.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    grade = list(input().split())

    a=0
    b=0
    for i in grade:
        a = grade.count(i)
        # print(a)
        if a > b:
            b = a
    print(f"#{tc} {b}")
# ????