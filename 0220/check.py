# 민석이의 과제 체크하기
import sys
sys.stdin = open('input05.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())  # n 수강생의 수, k 과제 제출한 사람의 수
    nums = list(map(int, input().split()))  # 제출한 사람들의 번호

    result = ""
    for i in range(1, n+1):
        if i not in nums:
            result += str(i) + " "
    print(f"#{tc} {result}")



