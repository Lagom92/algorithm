# 중간 평균값 구하기

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    N = sum(nums)
    N = N - max(nums) - min(nums)
    result = round(N/8)

    print(f"#{tc} {result}")