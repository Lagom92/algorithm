import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    num = list(map(int, input().split()))

    num = [0] + num +[N]
    # print(num)
    count = 0
    a=0
    b=[]

    for i in range(0, M+1):
        a = num[i+1] - num[i]
        b.append(a)
    # print(b)

    for j in range(0, M):
        if b[j] + b[j+1] > K:
            count += 1
        elif b[j] + b[j+1] > K*2:
            count = -1


    print(f"#{test_case} {count}")
