import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    tc, N = input().split()
    word = input()

    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = ""

    for i in range(10):
        cnt = 0
        if nums[i] in word:
            if nums[i] not in result:
                cnt = word.count(nums[i])
                result += (nums[i]+" ") * cnt
    print(tc)
    print(result)
