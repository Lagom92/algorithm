T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    print("#{}".format(test_case))
    for i in range(N):
        for j in range(i + 1):
            if j != 0 and j != i:
                print(i, end=" ")
            else:
                print("1", end=" ")
        print()