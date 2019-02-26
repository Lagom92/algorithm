# 세상의 모든 팰린드롬

T = int(input())
for tc in range(1, T+1):
    word = input()
    if word == word[::-1]:
        result = "Exist"
    else:
        result = "Not exist"
        print(word)
        print(word[::-1])

    print(f"#{tc} {result}")