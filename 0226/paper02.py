# 기본 피보나치 재귀
def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-1) + paper(n-2)

print(paper(6))