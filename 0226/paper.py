# 종이 붙이기
# 피보나치 변형 문제
T = int(input())
def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-1) + paper(n-2)*2

for tc in range(1, T+1):
    N = int(input())
    n = N//10
    result = paper(n)
    print(f"#{tc} {result}")





