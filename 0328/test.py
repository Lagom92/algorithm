N = int(input())
table = [list(map(int, input().split())) for x in range(N)]

print(N)
print(table)
a = [[0.01]*N for k in range(N)]
print(a)
for i in range(N):
    for j in range(N):
        table[i][j] *= 0.01
print(table)