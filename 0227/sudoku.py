# 스도쿠 검증
import sys
sys.stdin = open('input04_sample.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for x in range(9)]

    result = 1
    for i in range(9):
        for j in range(9):
            if sudoku[i].count(sudoku[i][j]) > 1:  # 가로 검사
                result = 0
                break

            elif sudoku[j].count(sudoku[j][i]) > 1:   # 세로 검사
                result = 0
                break

    for m in range(0, 7, 3):
        for n in range(0, 7, 3):
            a = []
            for o in range(3):
                for p in range(3):
                    a.append(sudoku[m+o][n+p])

            for i in range(9):
                if a.count(a[i]) > 1:
                    result = 0
                    break
            break

    print(f"#{tc} {result}")

