import sys
sys.stdin = open('input01.txt','r')

def lvr(n):
    if n>0:
        lvr(ch1[n])
        print(s[n], end="")
        lvr(ch2[n])

for tc in range(1, 11):
    N = int(input())
    ch1 = [0]*(N+1)
    ch2 = [0] * (N + 1)
    tree = [0]*(N+1)
    s = [0] * (N + 1)
    for i in range(N):
        node = list(input().split())
        if len(node) == 4:
            ch1[int(node(0))] = int(node[2])
        elif len(node) == 3:
            ch1[int(node(0))] = int(node[2])



