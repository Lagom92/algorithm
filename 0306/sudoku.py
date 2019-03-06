# 스도쿠 검증
import sys
sys.stdin = open('input01.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for x in range(9)]

    # print(sudoku)

    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 1

    for i in range(9):
        a = []
        b = []
        for j in range(9):
            a.append(sudoku[i][j])
            b.append(sudoku[j][i])

        a.sort()
        b.sort()
        # print(a)
        # print(b)
        if a == n:
            result = 1
        else:
            result = 0

        if b == n:
            result = 1
        else:
            result = 0

    for o in range(0, 7, 3):
        for p in range(0, 7, 3):
            c = []
            for m in range(3):
                for n in range(3):
                    c.append(sudoku[m+o][n+p])
            c.sort()
            if c == n:
                result = 1
            else:
                result = 0

    print(result)
