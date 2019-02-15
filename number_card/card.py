import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    card = int(input())

    maxK = 0
    maxV = 0

    # 무슨 카드가 몇개 있는지 나타내는 딕셔너리
    result = {}
    for i in range(N):
        a = card % 10
        card = card // 10
        if a in result:
            result[a] += 1
        else:
            result[a] = 1

    for key in result.keys():
        if result[key] > maxV:
            maxV = result[key]
            maxK = key
        if result[key] == maxV:
            if maxK < key:
                maxK = key
                result[key] += 1

    print(f"#{test_case} {maxK} {maxV}")