# 약수 구하는 방법
n = int(input())
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=" ")
        # if i%2 == 1:    # 홀수만
        #     print(i, end=" ")