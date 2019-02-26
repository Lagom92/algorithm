# 반복문자 지우기
import sys
sys.stdin = open('input02.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    words = input()

    box = []
    box.append(words[0])
    for i in range(1, len(words)):
        if len(box) != 0:
            if box[-1] == words[i]:
                box.pop(-1)
            else:
                box.append(words[i])
        else:
            box.append(words[i])
    print(f"#{tc} {len(box)}")