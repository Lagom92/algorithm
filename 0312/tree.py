# tree 연습문제1_쌤

# 13 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13


def vlr(n): #전위순회
    if(n>0):
        print(n, end=' ')
        vlr(ch1[n]) # 왼쪽 자식으로 이동
        vlr(ch2[n]) # 오른쪽 자식으로 이동
    return

def lvr(n): #중위순회
    if(n>0):
        lvr(ch1[n]) # 왼쪽 자식으로 이동
        print(n, end=' ')
        lvr(ch2[n]) # 오른쪽 자식으로 이동
    return

def lrv(n): #후위순회
    if(n>0):
        lrv(ch1[n]) # 왼쪽 자식으로 이동
        lrv(ch2[n]) # 오른쪽 자식으로 이동
        print(n, end=' ')
    return

def dlr(n):
    print(n, end=' ')
    if(ch1[n]>0):
        dlr(ch1[n])  # 왼쪽 자식으로 이동
    if(ch2[n]>0):
        dlr(ch2[n])  # 오른쪽 자식으로 이동


# import sys
# sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())   # V 정점의 총 수, E 간선의 수
node = list(map(int, input().split()))

ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
for i in range(E):
    n1 = node[i*2]
    n2 = node[i*2+1]
    if(ch1[n1]==0):
        ch1[n1] = n2
    else:
        ch2[n1] = n2

vlr(1)
print()
vlr(2)
print()

lvr(1)
print()
lrv(1)
print()