# 조합
# for 이용

a = [1,2,3,4,5,6]
cnt = 0
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1,len(a)):
            print(a[i],a[j],a[k])
            cnt += 1
print(cnt)