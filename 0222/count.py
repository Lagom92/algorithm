# 글자수 문제
import sys
sys.stdin = open('input03.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if result < cnt:
            result = cnt

    print(f"#{tc} {result}")