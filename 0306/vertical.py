# 의석이의 세로로 말해요
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    words = [input() for x in range(5)]

    result = ""
    num = 0

    for k in range(5):
        if num < len(words[k]):
            num = len(words[k])

    for i in range(5):
        if len(words[i]) < num:
            words[i] = words[i] + "-" * (num-len(words[i]))

    for i in range(num):
        for j in range(5):
                result += words[j][i]
    result = result.replace("-", "")
    print('#{} {}'.format(tc, result))
