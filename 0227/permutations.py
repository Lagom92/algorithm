from itertools import permutations

mylist = [1, 2, 3]

a = permutations(mylist)
for i in a:
    print(i)

print("---")

N = 3
arr = [4, 8, 9]
for j in permutations(range(N)):
    # print(j)
    print(arr[j[0]], arr[j[1]], arr[j[2]])
    