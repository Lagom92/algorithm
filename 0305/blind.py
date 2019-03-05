# 블라인드_백

M, N = map(int, input().split())
tower = [input() for x in range(5*M+1)]

blind = {'16': 0, '12': 0, '8': 0, '4': 0, '0': 0}

a = []
for m in range(0, M*5, 5):
    for n in range(0, N*5, 5):
        cnt = 0
        for i in range(1, 5):
            for j in range(1, 5):
                if tower[i+m][j+n] == ".":
                    cnt += 1
        a.append(str(cnt))

for k in range(M*N):
    blind[a[k]] += 1

for p in range(0, 17, 4):
    print(blind[str(p)], end=" ")
