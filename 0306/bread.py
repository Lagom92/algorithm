# 두가지 빵의 딜레마

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    cnt = 0
    if A < B:   # 보통 A가 B보다 비싸다라고 가정하고 B가 더 크면 A 와 B를 바꿔줌
        A, B = B, A

    while C > A:
