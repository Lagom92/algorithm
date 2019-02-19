import sys
sys.stdin = open('input01.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count = 0

    for i in range(1, 2**12):
        result = []
        s = 0
        for j in range(12):
            if i & (1 << j) != 0:
                s += A[j]
                result.append(A[j])
        if s == K:
            if len(result) == N:
                count += 1
    print(f"#{test_case} {count}")
