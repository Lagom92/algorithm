# 이진탐색
import sys
sys.stdin = open('input04.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    book, targetA, targetB = map(int, input().split())

    left = 1
    right = book
    cntA = 0
    while left < right:  # A 이진탐색
        mid = (left + right) // 2
        cntA += 1
        if mid == targetA:
            break
        elif mid > targetA:
            right = mid
        else:
            left = mid

    left = 1
    right = book
    cntB = 0
    while left < right:  # B 이진탐색
        mid = (left + right) // 2
        cntB += 1
        if mid == targetB:
            break
        elif mid > targetB:
            right = mid
        else:
            left = mid

    if cntA < cntB:  # 이진탐색 횟수 비교
        print(f"#{tc} A")
    elif cntA > cntB:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")