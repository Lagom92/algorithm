# 가능한 시험 점수
# 시간초과 발생
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))

    res = set()

    for i in range(2 ** N):    # 부분집합 구하기
        # i를 비트 단위로 접근
        s = 0
        for j in range(N - 1, -1, -1):
            if (i & (1 << j) != 0):  # score[j]가 포함되면
                s += score[j]
        res.add(s)
    print('#{} {}'.format(tc, len(res)))