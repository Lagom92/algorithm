# 조교의 성적 매기기
import sys
sys.stdin = open('input02.txt','r')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    grade = ["A+", "A0", "A-", "B+", "B0", "B-",
             "C+", "C0", "C-", "D0"]
    total = 0
    a =[]
    student = 0
    for i in range(N):
        total = (arr[i][0]*0.35) + (arr[i][1]*0.45) + (arr[i][2]*0.2)
        a.append(total)
    student = a[K-1]
    a.sort(reverse=True)
    idx = a.index(student)
    result = grade[idx // (N//10)]
    print('#{} {}'.format(tc, result))