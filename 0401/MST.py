# 최소 신장 트리
# KRUSKAL 알고리즘

def MST_KRUSKAL(G, w):
    pass


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    arr = [list(map(int, input().split())) for x in range(E)]

    arr.sort(key= lambda i:i[2])
    print(arr)

