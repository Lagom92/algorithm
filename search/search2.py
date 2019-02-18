# 정렬되어 있는 경우
# 이진 검색

def bs(arr, n, key):
    start = 0
    end = n-1

    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            return 1
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1

A = [7, 2, 4, 3, 5, 8, 9]
A.sort()
print(A)

print(bs(A, len(A), 4))
print(bs(A, len(A), 11))
