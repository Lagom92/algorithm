# 괄호의 짝 검사하기
import sys
sys.stdin = open('input_ex2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    b = input()
    s = []
    for i in range(len(b)):
        if b[i] == "(":  # push
            s.append(i)
        elif b[i] == ")":  # pop
            if len(b) == 0:
                print(-1)
                break
            s.pop(-1)

    print(f"#{tc}", end=" ")
    if len(s) != 0:
        print(-1)
        # print(s)
    else:
        print(1)
        # print(s)


