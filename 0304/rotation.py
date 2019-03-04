# 회전
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    nums = list(map(int, input().split()))

    for i in range(M):
        a = nums.pop(0)
        nums.append(a)

    print('#{} {}'.format(tc, nums[0]))