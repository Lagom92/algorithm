arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]

# 입력된 배열
# for i in arr:
#     print(i)

# 한 줄 만들기
one_line = []
for i in range(len(arr)):
    for j in range(len(arr[0])):
        one_line.append(arr[i][j])

# 정렬하기
for i in range(len(one_line)-1):
    min_num = i
    for j in range(i+1, len(one_line)):
        if one_line[min_num] > one_line[j]:
            min_num = j
    one_line[i], one_line[min_num] = one_line[min_num], one_line[i]

# print()
# print(one_line)
# print()

# 시계방향 달팽이
i = 0
j = -1
f = len(arr)
c = 1
num = -1

while True:
    for n in range(f):
        num += 1
        j += c
        arr[i][j] = one_line[num]
    f -= 1
    if f <= 0:
        break
    for n in range(f):
        num += 1
        i += c
        arr[i][j] = one_line[num]
    c *= -1

# 달팽이 배열 출력
for i in arr:
    print(i)
