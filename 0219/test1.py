# 웹에선 잘 동작함 ??
import sys
sys.stdin = open('test_input.txt', 'r')

for i in range(10):
    T = int(input())
    word = input()
    words = input()

    a = words.split(word)
    cnt = len(a)-1

print(f"#{T} {cnt}")