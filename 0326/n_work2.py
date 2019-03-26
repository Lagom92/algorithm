# a,b,c 사람이 3개의 일을 각자 하나씩 할때 최소 값은 무엇인가??
# 순열 이용
# 최소 비용 찾는 문제
# by 쌤


def f(n, k, s):
    global minV, cnt
    cnt += 1
    if n == k:
        if s < minV:
            minV = s
    elif s >= minV:
        return
    else:
        for i in range(K):
            if u[i] == 0:    # i번 일을 맡은 사람이 아직 없으면
                u[i] = 1   # i번 일이 배정되었음을 기록
                f(n+1, k, s+m[n][i])   # n번 사람이 i번 일을 하는데 걸리는 시간을 추가, n+1 사람의 일을 배정하러 이동
                u[i] = 0    # i번 일을 다른 사람에게 배정할 수 있도록 풀어줌


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    m = [list(map(int, input().split())) for i in range(K)]
    u = [0] * K    # 배정된 일은 1로 표시
    minV = 10000000
    cnt = 0
    f(0, K, 0)
    print(minV)
    print(cnt)