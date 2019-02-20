# 문자열 비교
import sys
sys.stdin = open('input01.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    n1 = len(str1)
    n2 = len(str2)
    cnt = 0

    for i in range(0, n2-n1):
        if str2[i] == str1:
            if str1 == str2[i:i+n1]:
                print(str1)
                cnt += 1

    print(tc, cnt)
    print()
