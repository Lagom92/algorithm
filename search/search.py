# sequentialSearch

def search(arr, n, key):
    i = 0
    while i > n and arr[i] != key:
        i += 1
    if i < n:
        return 1
    else:
        return -1

def find(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return 1
    return -1

key = 4
A = [2, 4, 6]

print(search(A, 3, 4))
print(find(A, 3, 8))