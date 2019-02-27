# forth
import sys
sys.stdin = open('input01.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    code = input().split()

    box = []
    a = 0
    b = 0
    result = ""
    for i in code:
        if i.isdigit():
            box.append(i)   # 숫자만 넣은 box
        else:
            if len(box) >= 2:   # box 에 2개 이상 있으면
                a = box.pop(-1)
                b = box.pop(-1)
            elif len(box) < 1:
                result = "error"
                break
            if i == "+":
                result = int(b)+int(a)
                box.append(result)
            elif i == "-":
                result = int(b) - int(a)
                box.append(result)
            elif i == "*":
                result = int(b) * int(a)
                box.append(result)
            elif i =="/" and int(a) == 0:
                result = "error"
                break
            elif i == "/":
                result = int(b) // int(a)
                box.append(result)

        if i == ".":
            if len(box) == 1:
                result = box[0]
            else:
                result="error"


    print(f"#{tc} {result}")

