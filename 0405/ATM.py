N = int(input())
num = list(map(int, input().split()))
num.sort()
t = [0]*N
for i in range(N):
    t[i] = t[i-1] + num[i]
print(sum(t))