import sys
sys.stdin = open('input01.txt','r')

def lvr(n, k):
    if n <= k:
        lvr(n*2, k)
        print(tree[n], end="")
        lvr(n*2+1, k)

for tc in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)

    for i in range(N):
        node = list(input().split())
        tree[int(node[0])] = node[1]


