# 간단한 압축 풀기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    word = [input().split() for x in range(N)]

    result =""
    for i in range(N):
        result += word[i][0] * int(word[i][1])

    print('#{}'.format(tc), end="")
    for j in range(len(result)):
        if j % 10 == 0:
            print()
        print(result[j], end="")
    print()


