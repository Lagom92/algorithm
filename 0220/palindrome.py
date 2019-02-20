# 초심자의 회문검사
import sys
sys.stdin = open('input04.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    word = input()
    wordR = word[::-1]  # 입력받은 문자를 거꾸로 읽음
    cnt = 1 if word == wordR else 0  # 회문이면 1, 아니면 0
    print(f"#{tc} {cnt}")