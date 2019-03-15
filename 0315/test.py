def s(n):
    return 1 if n==1 else n+s(n-1)
print(s(int(input())))
