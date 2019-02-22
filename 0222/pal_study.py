# 회문을 공부하자

import sys
sys.stdin = open('sample_input02.txt', 'r')
tc = int(input())

arr = [list(input().split()) for i in range(8)]
print(arr)
m = 4
n = 8
for i in range(n):   # [ [*], [], [] ...] 에서 [*] 선택
    print("m 개씩 출력")
    for j in range(n-m+1):   #
        a=""
        a = "".join(arr[i])[j:j + m]  # join(리스트를 문자열로)
        # print(a)
        print("---")

        for k in range(n-m+1):  # 세로로 m 개씩 출력
            b=""
            for k in range(m):
                b += "".join(arr[j + k])[i]
        print(b)
