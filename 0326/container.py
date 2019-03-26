# 컨테이너 운반
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # 컨테이너 수 N, 트럭 수 M
    W = list(map(int, input().split()))   # 화물 무게 W
    T = list(map(int, input().split()))   # 적재용량 T

    T.sort(reverse=True)    # 내림차순으로 정리
    W.sort(reverse=True)

    maxT = 0
    maxW = 0
    res = 0

    c = M if N > M else N   # M 과 N 중 더 작은 수 찾기

    for i in range(c):   # 가장 큰 T 와 W 비교
        maxT = T[0]
        T.pop(0)
        maxW = W[0]
        W.pop(0)

        if maxT >= maxW:
            res += maxW
        else:   # 화물을 트럭에 못 넣을 경우 트럭만 재사용
            T.insert(0, maxT)

    print('#{} {}'.format(tc, res))