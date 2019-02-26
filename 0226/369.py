# 간단한 369 게임

N = int(input())

result = ""
for i in range(1, N+1):

    s=""
    while i > 0:
        cnt = 0
        a = i % 10
        i = a // 10
    if a == 3 or a == 6 or a == 9:
        a = "-"
        result = result + a + " "

    else:
        result = result + str(a) + " "
print(result)

