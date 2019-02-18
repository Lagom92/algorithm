# 부분집합 만들기
A = [1, 2, 3]
N = 3

for i in range(2**N):
    # i를 비트 단위로 접근
    for j in range(N-1, -1, -1):
        if i & (1 << j) != 0:  # i 의 j번 비트 검사, A[j]가 포함되면
            print(A[j], end="")
    print()

# 방식2
for i in range(2**N):
    # i를 비트 단위로 접근
    for j in range(N):
        if i & (1 << j) != 0:  # i 의 j번 비트 검사, A[j]가 포함되면
            print(A[j], end="")
    print()

# 부분집합의 합
for i in range(2**N):
    s = 0
    # i를 비트 단위로 접근
    for j in range(N):
        if i & (1 << j) != 0:  # i 의 j번 비트 검사, A[j]가 포함되면
            s += A[j]
            print(A[j], end="")

    print(s)
    print()