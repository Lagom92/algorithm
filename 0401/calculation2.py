# 연산_front, rear 이용
def bfs(n, m):
    v = [0] * 1000001    # 방문 기록
    q = [0] * 1000001
    front = -1
    rear = -1

    rear += 1
    q[rear] = n   # 큐에 시작 노드 인큐

    while front != rear:    # 큐가 비어있지 않으면
        front += 1
        n = q[front]    # 다음 노드를 꺼내

        if n == m:    # 찾는 노드인 경우 거리 리턴
            return v[n]

        t = [n-10, n-1, n+1, n*2]    # 인접 노드번호 계산
        for i in range(4):
            if t[i] >0 and t[i] <= 1000000:    # 유효한 노드 번호이면
                if v[t[i]] == 0:
                    v[t[i]] = v[n] + 1    # 거리를 기록하고
                    rear += 1
                    q[rear] = t[i]    # 큐에 추가


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = bfs(N, M)
    print('#{} {}'.format(tc, res))