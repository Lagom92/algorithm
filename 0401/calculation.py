# 연산
# 시간 초과가 남 => front, rear로 해야할듯
T = int(input())

def f(n, M):
    q = []
    visited = [0]*1000001
    q.append(n)
    visited[n] = 1

    while q:
        x = q.pop(0)

        if x == M:
            return visited[M] - 1

        if x+1 <=1000000 and visited[x+1] == 0:
            q.append(x+1)
            visited[x+1] = visited[x] + 1

        if x-1 >=1 and visited[x-1] == 0:
            q.append(x-1)
            visited[x-1] = visited[x] + 1

        if x*2 <=1000000 and visited[x*2] == 0:
            q.append(x*2)
            visited[x*2] = visited[x] + 1

        if n-10 >=1 and visited[x-10] == 0:
            q.append(x-10)
            visited[x-10] = visited[x] + 1
    return 0


for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = f(N, M)

    print('#{} {}'.format(tc, res))