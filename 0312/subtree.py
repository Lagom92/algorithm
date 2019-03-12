T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    nodeP = []
    nodeC = []
    box = []
    for x in range(E*2):
        if x % 2 == 0:
            nodeP.append(node[x])
        else:
            nodeC.append(node[x])
    box.append(N)
    if N in nodeP:
        while box[-1] in nodeP:
            a = nodeP.index(box[-1])
            box.append(nodeC[a])

    print('#{} {}'.format(tc, len(box)))

