# 가능한 시험 점수
# 성공_공부해보자
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    u = [0]*N*101    # 사용표시
    res = [0]    # 결과값
    cnt = 1    # 경우의 수
    for i in range(N):
        for j in range(len(res)):
            num = score[i] + res[j]
            if u[num] == 0:    # 이미 출력된 숫자가 아니면
                u[num] = 1
                res.append(num)
                cnt += 1
    print('#{} {}'.format(tc, cnt))