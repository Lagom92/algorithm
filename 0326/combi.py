# 조합
# 재귀 이용

def ncr(n, r):
    global cnt
    if r == 0:
        print(tr)
        cnt += 1
    elif n < r:
        return
    else:
        tr[r-1] = a[n-1]
        ncr(n-1, r-1)   # 포함
        ncr(n-1, r)     # 미포함

tr = [0]*3
a = [1,2,3,4,5,6]
cnt = 0
ncr(6,3)
print(cnt)