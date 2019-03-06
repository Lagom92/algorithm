# 오르막길_백
N = int(input())
nums = list(map(int, input().split()))

box = [0]
a = 0
for i in range(1, N):
    if nums[i] > nums[i-1]:
        a += nums[i] - nums[i-1]
    else:
        box.append(a)
        a = 0
if a > 0:
    box.append(a)
print(max(box))



