from itertools import permutations

mylist = [1, 2, 3]

a = permutations(mylist)
for i in a:
    print(i)

print("---")

N = 3
for j in permutations(range(N)):
    print(j)