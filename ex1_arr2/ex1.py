# 연습문제 1
N = 5
A = [[38, 79, 1, 73, 44], [17, 76, 36, 63, 92], [7, 46, 30, 67, 19], [20, 86, 46, 47, 46], [1, 7, 81, 26, 63]]

# 오른쪽부터 시계방향으로
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

result = 0
for i in range(N):
    for j in range(N):  # 배열 A의 모든 원소에 대해
        # print(i, j, end=" ")  # k번 방향 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:  # 배열을 벗어나지 않는 경우
                # print(A[ni][nj], end=" ")
                result = result + abs(A[ni][nj] - A[i][j])

print(f"총합: {result}")