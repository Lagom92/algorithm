# 패턴 마디의 길이

T = int(input())
for tc in range(1, T+1):
    word = input()
    result = 0
    for i in range(1, 11):
        if word[0:i] == word[i:i*2]:
            result = i
            break

    print('#{} {}'.format(tc, result))