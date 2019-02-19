# 선택 정렬
import sys
sys.stdin = open('input03.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N개의 정수
    nums = list(map(int, input().split()))  # 주어진 숫자 리스트

    for i in range(0, N-1):
        minIdx = i
        maxIdx = i
        if i % 2 == 0:  # 짝수번째, 내림차순
            for j in range(i+1, N):
                if nums[minIdx] < nums[j]:
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
        else:  # 홀수번째, 오름차순
            for j in range(i+1, N):
                if nums[maxIdx] > nums[j]:
                    maxIdx = j
            nums[i], nums[maxIdx] = nums[maxIdx], nums[i]

    print(f"#{tc}", end=" ")
    for n in range(10):  # nums 리스트 중에서 10개만 결과로 출력
        print(nums[n], end=" ")
    print()






