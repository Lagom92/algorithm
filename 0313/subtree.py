# subtree
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    nodeP = []
    nodeC = []
    box = []

    for x in range(E*2):   # 부모와 자식 구분시킴
        if x % 2 == 0:
            nodeP.append(node[x])
        else:
            nodeC.append(node[x])

    box.append(N)

    for i in range(E):
        for j in range(len(box)):
            if nodeP[i] == N or nodeP[i] == box[j]:   # nodeP에 있는 값이 N 이거나 box에 있는 값이면
                if nodeC[i] not in box:   # 이미 box 에 넣어진 값이 아니면
                    box.append(nodeC[i])
    print('#{} {}'.format(tc, len(box)))