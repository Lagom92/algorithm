# 2중 배열에서 계단 모양으로 값들 출력 하기

arr = [[1,2,3], [4,5,6], [7,8,9]]

print(arr)
# 1 2 3
# 4 5 6
# 7 8 9

for i in range(3):
    for j in range(3):

        if i <= j:   # 오른쪽 위 모음
            print(arr[i][j])
            # 1 2 3 5 6 9

        if i >= j:    # 왼쪽 아래 모음
            print(arr[i][j])
            # 1 4 5 7 8 9

        if i <= 3-j-1:   # 왼쪽 위 모음
            print(arr[i][j])
            # 1 2 3 4 5 7

        if i >= 3-j-1:   # 오른쪽 아래 모음
            print(arr[i][j])
            # 3 5 6 7 8 9

