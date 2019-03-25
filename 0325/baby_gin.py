def npr(n, k):   # n이 순열의 길이, k는 숫자를 결정할 자리
    if n == k:
        # print(p)
        r = 0
        t = 0
        if p[0] == p[1]+1 and p[1] == p[2]+1:
            r += 1
        if p[0] == p[1] == p[2]:
            t += 1
        if p[3] == p[4]+1 and p[4] == p[5]+1:
            r += 1
        if p[3] == p[4] == p[5]:
            t += 1
        if r+t == 2:
            return 1
    else:
        for i in range(k, n):
            p[i], p[k] = p[k], p[i]
            npr(n, k+1)
            p[i], p[k] = p[k], p[i]

p = [0, 5, 4, 0, 6, 0]
npr(6, 0)