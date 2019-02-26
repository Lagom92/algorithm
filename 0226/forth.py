# Forth
import sys
sys.stdin = open('input04.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    code = input().split()
    box = []
    a = 0
    b = 0
    result = 0
    for i in code:
        if i.isdigit():
            box.append(i)
        else:
            if len(box) >= 2:
                a = box.pop(-1)
                b = box.pop(-1)
            if i == "+":
                result = int(b)+int(a)
                box.append(result)
            elif i == "-":
                result = int(b) - int(a)
                box.append(result)
            elif i == "*":
                result = int(b) * int(a)
                box.append(result)
            elif i == "/":
                result = int(b) // int(a)
                box.append(result)
    if len(box) == 0:
        result = "error"
    if code[-1] != ".":
        result = "error"

    print(f"#{tc} {result}")