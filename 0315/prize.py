# 최대 상금
# 미완성
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1, T+1):
    N, cnt = list(map(int, input().split()))

    num = []
    for x in str(N):   # 123 -> ['1','2','3']
        num.append(x)
    result = []
    # print(num)

    while cnt > 0:    # 주어진 횟수만큼 시행
        if len(num) > 2:
            maxV = max(num)    # 최대값 구하기
            num.reverse()   # 가장 뒤에 있는 최대값의 인덱스 구하기
            idx = num.index(maxV)
            idx = len(num)-1 - idx
            num.reverse()

            if num[idx] != num[0]:   # 0번째 값이랑 최대값이 다르면
                num[idx], num[0] = num[0], num[idx]
                result.append(num[0])
                num.pop(0)
                cnt -= 1
            else:   # 0번째 값이랑 최대값이 같으면 다음 꺼를 옮겨야함
                result.append(num[0])
                num.pop(0)
        else:
            num[0], num[1] = num[1], num[0]
            cnt -= 1

    result = result + num
    print('#{}'.format(tc), end=" ")
    print(''.join(result))