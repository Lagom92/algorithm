# reverse 함수 혹은 slice notation
# 확장형 슬라이스
s = "python is short"
print(s)

rs = s[::-1]
print(rs)

ss = s[::2]
print(ss)

print()
# 회문
a = "lol"
b = a[::-1]
print(a, b)
if a==b:
    print("ㅇ")
else:
    print("n")