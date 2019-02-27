def npk(n, k):
    if n == k:
        print(p)
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                p[n] = a[i]
                npk(n+1, k)
                used[i] = 0
a = [1, 2, 3, 4, 5]
K=len(a)
p=[0]*K
used=[0]*K
npk(0, K)