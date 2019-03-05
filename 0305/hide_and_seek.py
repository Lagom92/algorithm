# 숨바꼭질_백

def bfs(n, k):
    q = []
    visited = [0]*100001
    q.append(n)
    visited[n] = 1

    while len(q) != 0:
        n = q.pop(0)
        if n == k:
            return visited[k]-1
        # 인접에 관해
        # n-1
        if n-1 >= 0 and visited[n-1] == 0:  #  and 좌우 순서 중요! 바꾸면 에러나옴
            q.append(n-1)
            visited[n-1] = visited[n] + 1
        # n+1
        if n+1 <= 100000 and visited[n+1] == 0:
            q.append(n+1)
            visited[n+1] = visited[n] + 1
        # n*2
        if n*2 <= 100000 and visited[n*2] == 0:
            q.append(n*2)
            visited[n*2] = visited[n] + 1
    return 0

N, K = map(int, input().split())

print(bfs(N, K))