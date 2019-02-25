import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for x in range(N)]
    cnt = 0
    for i in range(N):
        a = []
        s = []
        for j in range(N):   # 세로로 탐색 후  a 에 저장
            a.append(table[j][i])
        for k in a:     # 리스트에서 1과 2만 넣기
            if k == 1:
                s.append(k)
            elif k == 2:
                s.append(k)
        for m in range(len(s)-1):   # 1 다음 2 가 나오면 cnt + 1 하기
            if s[m] == 1 and s[m+1] == 2:
                cnt += 1

    print(f"#{test_case} {cnt}")
