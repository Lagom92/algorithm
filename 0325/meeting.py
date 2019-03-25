# 회의실 배정하기
a = [[1,4], [1,6], [6,10], [5,7], [3,8], [5,9], [3,5], [8,11], [2,13], [12,14],]

a.sort(key=lambda x:x[0])
print(a)
a.sort(key=lambda x:x[1])   # 끝나는 시간 순으로 정렬함
print(a)

m = []   # 열리는 회의 정보
end = 0
for i in range(len(a)):
    if a[i][0] >= end:   # 앞의 회의가 끝난 후 시작하면
        end = a[i][1]
        m.append(a[i])
print(m)
print(len(m))