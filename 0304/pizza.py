# 피자 굽기
import sys
sys.stdin = open('input03.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    pizzas = list(map(int, input().split()))

    que = []
    front = N-1
    flag = [x+1 for x in range(M)]
    print(N, M)
    print(pizzas)
    print(flag)
    for j in range(N-1):
        que.append(pizzas[j])


    a = 0
    b = 0
    while len(que) != 1:
        if len(que) < N:
            if front < M:
                que.append(pizzas[front])
                front += 1
        que[0] = que[0] // 2

        if que[0] == 0:   # que 맨 앞이 0 이면 pop
            que.pop(0)


        a = que.pop(0)   # que 에 맨 앞을 맨 뒤로이동
        que.append(a)

    # print(que)


    print()
    print()

