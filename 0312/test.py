V, E = map(int, input().split())   # V 정점의 총 수, E 간선의 수
node = list(map(int, input().split()))

def lvr(n): #중위순회
    if(n>0):
        lvr(ch1[n]) # 왼쪽 자식으로 이동
        print(n, end=' ')
        lvr(ch2[n]) # 오른쪽 자식으로 이동
    return


ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
for i in range(E):
    n1 = node[i*2]
    n2 = node[i*2+1]
    if(ch1[n1]==0):
        ch1[n1] = n2
    else:
        ch2[n1] = n2

lvr(1)
