
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = 10
cnt = 0
for i in range(0, (1<<n)):
    res = []
    for j in range(0, n):
        if i & (1<<j):
            # print(arr[j], end=" ")
            res.append(arr[j])
    if sum(res) == 0:
        print(res)
        cnt += 1
print(cnt)

