import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    H = list(map(int, input().split()))

    top = 0
    bottom = 101

    for i in H:
        while N > 0:
            N = N - 1
            if top < i:
                top = i
                i -= 1
            elif bottom > i:
                bottom = i
                i += 1

    print(top)
    print(bottom)
    print(top-bottom)

