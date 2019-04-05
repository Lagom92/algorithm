N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.sort(reverse=True)
cnt = 0
for i in range(N):
    if K >= coin[i]:
        cnt += K // coin[i]
        K = K % coin[i]
print(cnt)