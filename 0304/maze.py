# 미로
# 출발에서 도착까지 갈수 있으면 1 없으면 0

import sys
sys.stdin = open('input01.txt', 'r')

def f(i, j, n):
    di = [0, 1, 0, -1]   # 위, 오른쪽, 아래, 왼쪽
    dj = [1, 0, -1, 0]

    if maze[i][j] == 3:   # 목적지에 도착한 경우
        return 1
    else:  # 목적지 아님, 계속 탐색
        maze[i][j] = 1   # 방문한 칸으로 미로에 직접 표시, 다시 지나가지 않게 하기 위해서 1로 만듬
        for k in range(4):   # 주변 칸의 좌표 계산
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < n and nj >= 0 and nj < n:   # 미로를 벗어나지 않으면
                if maze[ni][nj] != 1:   # ni, nj 칸이 벽이 아니면 이동
                    r = f(ni, nj, n)
                    if r == 1:   # 목적지에 도착한 경우
                        return 1
        return 0   # 가능한 모든 방향에서 목적지를 찾지 못하면



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for x in range(N)]   # 문자열로 저장하는 경우 방문표시 배열
    # maze = [input() for x in range(N)]
    starti = -1
    startj = -1

    for m in range(N):
        for n in range(N):
            if maze[m][n] == 2:
                starti = m
                startj = n
                break
        if starti != -1:
            break

    # print(f"#{tc} {f(starti, startj, N)}")
    result = f(starti, startj, N)
    print('#{} {}'.format(tc, result))