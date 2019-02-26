#  괄호검사
import sys
sys.stdin = open('input01.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    words = input()
    box = []
    check = []
    for i in words:
        if i == "(" or i == "{":   # box 에 push
            box.append(i)
        elif i == ")" or i == "}":   # box 에서 pull
            if len(box) != 0:
                check.append(box[-1])
                box.pop(-1)
            else:
                result = 0
                break
            if i == ")" and check[-1] == "{":
                result = 0
                break
            elif i == "(" and check[-1] == "}":
                result = 0
                break
            elif i == "}" and check[-1] == "(":
                result = 0
                break
            elif i == "{" and check[-1] == ")":
                result = 0
                break

        if len(box) == 0:
            result = 1
        else:
            result = 0
    print(f"#{tc} {result}")