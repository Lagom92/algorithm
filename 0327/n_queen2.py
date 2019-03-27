# n queen _ 백_9663
def f(i, N):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if lr[i+N-j-1] == 0 and rl[i+j] == 0 and col[j] == 0:
                lr[i + N - j - 1] = 1
                rl[i + j] = 1
                col[j] = 1

                f(i+1, N)

                lr[i + N - j - 1] = 0   # 복구
                rl[i + j] = 0
                col[j] = 0

N = int(input())
cnt = 0
col = [0]*N   # 세로 검사
lr = [0]*(2*N-1)   # 왼오 대각선 검사
rl = [0]*(2*N-1)   # 오왼 대각선 검사
f(0,N)

print(cnt)