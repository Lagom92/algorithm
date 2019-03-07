# 삼성시의 버스노선
import sys
sys.stdin = open('input03.txt', 'r')
# 확인용
import sys
sys.stdin = open('input03.txt', 'r')
for t in range(int(input())):
    bus = [0] * 5001
    res = []
    for n in range(int(input())):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            bus[i] += 1
    for p in range(int(input())):
        res.append(str(bus[int(input())]))
    print('#{} {}'.format(t + 1, ' '.join(res)))

# 확인용



