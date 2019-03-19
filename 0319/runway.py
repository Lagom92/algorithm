# 활주로 문제_쌤
# 런 렝스 기법 활용
import sys
sys.stdin = open('input.txt', 'r')

def check(code, n, x):

    if code[0][1] == n:  # 모두 같은 높이인 경우
        return 1
    else:
        for j in range(1, len(code)):
            if code[j][0] - code[j - 1][0] == 1:  # 1 높아지는 경우
                if code[j - 1][1] < x:  # 낮은쪽이 x보다 짧으면 건설 불가
                    return 0

            elif code[j][0] - code[j - 1][0] == -1:  # 1낮아지는 경우
                if code[j][1] < x:  # 낮은 쪽이 x보다 짧으면 건설 불가
                    return 0
                else:
                    code[j][1] -= x
            elif abs(code[j][0] - code[j - 1][0]) > 1:
                return 0
        return 1

def f(n, x):
    cnt = 0
    for i in range(n):
        code = []
        c = 1
        idx = 1
        for idx in range(1, n):   # 1줄의 높이 정보를 높이-폭으로 기록
            if(m[i][idx]==m[i][idx-1]):
                c += 1
            else:
                code.append([m[i][idx-1], c])
                c = 1
        code.append([m[i][n-1], c])
        cnt += check(code, n, x)
        code = []
        c = 1
        idx = 1
        for idx in range(1, n):  # 세로 1줄의 높이 정보를 높이-폭으로 기록
            if (m[idx][i] == m[idx - 1][i]):
                c += 1
            else:
                code.append([m[idx - 1][i], c])
                c = 1
        code.append([m[n - 1][i], c])
        cnt += check(code, n, x)
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    m = [list(map(int, input().split())) for i in range(N)]
    print('#{} {}'.format(tc, f(N, X)))
