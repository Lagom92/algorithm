import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for x in range(N)]
    cnt = 0

    for i in range(N):
        flag = 0
        for j in range(N):
            if table[j][i] == 1:
                flag = 1
            elif table[j][i] == 2 and flag == 1:
                cnt += 1
                flag = 0
    print(f"#{test_case} {cnt}")
