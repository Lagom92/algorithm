# 정렬
a = [[1, 4], [4, 2], [2, 3], [1, 3], [5, 1], [3, 2]]
a.sort(key=lambda x:x[0])
print(a)
a.sort(key=lambda x:x[1])
print(a)