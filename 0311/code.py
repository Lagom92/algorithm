a= [1, 2, 3, 4]
print(a.index(3))

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))

    s = nums.index(N)
    for i in range(K):
        s += M
        if s > N:
            s -= (N+1)

        number = (nums[s-1]) + (nums[s])
        nums.insert(s, number)
        print(nums)
        print(s)
        s = nums.index(number)
        print(s)

    print(nums)
