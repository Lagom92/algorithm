# 최빈수 구하기
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    grade = list(input().split())

    print(n)
    print(grade)
    a=0
    b=0
    for i in grade:
        a = grade.count(i)
        # print(a)
        if a > b:
            b = a
    print(a)
    print(b)