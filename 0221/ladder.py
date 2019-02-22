import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(10):
    tc = int(input())
    ladder = [[0] + list(map(int, input().split())) + [0] for i in range(100)]  # 좌우에 0을 추가
    goal = 0
    # print(ladder)

    for i in range(100):   # 도착지점 i 확인
        if ladder[99][i] == 2:
            goal = i
            print(i)
            print(tc)

# 나중에 다시
