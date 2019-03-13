T = int(input())

def lvr(n):
    global cnt
    if n>0:
        lvr(ch1[n])
        cnt +=1
        lvr(ch2[n])
    return

for tc in range(1, T+1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    cnt = 0
    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    for i in range(E):
        n1 = node[i*2]
        n2 = node[i*2+1]
        if ch1[n1] == 0:
            ch1[n1] = n2
        else:
            ch2[n1] = n2

    lvr(N)

    print('#{} {}'.format(tc, cnt))