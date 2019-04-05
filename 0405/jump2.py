# 점프_백
# by_호근
N = int(input())    # 게임판의 크기
board = [list(map(int, input().split())) for _ in range(N)]    # 게임판

v = [[0]*N for x in range(N)]    # 방문표시
v[0][0] = 1    # 시작위치를 1로

for i in range(N):
    for j in range(N):
        if v[i][j] != 0 and board[i][j] != 0:    # 점프가 가능한 곳 이면

            ni = i + board[i][j]    # 현재 자리의 값 만큼 점프
            nj = j + board[i][j]
            if 0 <= ni < N:    # 점프 가능 범위에 있으면
                v[ni][j] += v[i][j]
            if 0 <= nj < N:    # 점프 가능 범위에 있으면
                v[i][nj] += v[i][j]
print(v)
print(v[N-1][N-1])