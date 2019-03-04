# 세상의 모든 펠린드롬

T = int(input())
for tc in range(1, T + 1):
    word = input()
    if "?" in word:
        word =  word.replace("?", "")
    print(word)

    if word == word[::-1]:
        result = "Exist"
    else:
        result = "Not exist"

    print(f"#{tc} {result}")