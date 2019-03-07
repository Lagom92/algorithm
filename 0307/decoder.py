# Base64 Decoder

def f(s):   # 문자를 숫자로
    if ord('A') <= ord(s) and ord(s) <= ord('Z'):
        return ord(s) - ord('A')
    elif ord('a') <= ord(s) and ord(s) <= ord('z'):
        return ord(s) - ord('a') + 26
    elif ord('0') <= ord(s) and ord(s) <= ord('9'):
        return ord(s) - ord('1') + 52
    elif ord('+'):
        return 62
    elif ord('/'):
        return 63


words = "TGlm"
box = []
for word in words:
    num = f(word)
    box.append(bin(num))

print(box)
