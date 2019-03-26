import itertools

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    m = [list(map(int, input().split())) for i in range(K)]
    u = [0] * K    # 배정된 일은 1로 표시
    minV = 10000000
    print(m)
    print(list(itertools.permutations(m)))
