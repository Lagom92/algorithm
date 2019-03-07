N = int(input())
arr = [input() for x in range(N)]

print(N)
print(arr)
total = 0
for i in range(N):
    for j in range(N):
        if i + 1 <= j + 1:  # 왼쪽 아래
            print(arr[i][j])
            total += int(arr[i][j])

        if i + 1 <= j + 1:  # 오른 위
            print(arr[j][i])
            total += int(arr[j][i])

        if i <= j:  # 왼쪽 위
            print(arr[N - i - 1][j])
            total += int(arr[N - i - 1][j])

        if i <= j:  # 오른쪽 아래
            print(arr[N - j - 1][i])
            total += int(arr[N - j - 1][i])

print(total)


