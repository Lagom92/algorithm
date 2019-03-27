def merge_sort(a):
    global cnt
    if len(a) == 1:   # 숫자가 하나면 리턴
        return a
    else:
        middle = len(a)//2    # 숫자들의 가운데
        left = a[:middle]    # 리스트 왼쪽 절반
        right = a[middle:]    # 리스트 오른쪽 절반
        left = merge_sort(left)    # 정렬된 왼쪽 절반
        right = merge_sort(right)    # 정렬된 오른쪽 절반
        idxl = 0
        idxr = 0
        i = 0

        while idxl < len(left) and idxr < len(right):
            if left[idxl] < right[idxr]:    # 왼쪽 꺼, 오른쪽 꺼 비교 / 작은 것을 a에 넣기
                a[i] = left[idxl]
                idxl += 1
            else:
                a[i] = right[idxr]
                idxr += 1
            i += 1

        if left[-1] > right[-1]:    # 왼쪽 마지막이 오른쪽 마지막보다 큰 경우
            cnt += 1

        if idxl < len(left):    # 왼쪽 리스트가 남은 경우
            a[i:] = left[idxl:]
        if idxr < len(right):    # 오른쪽 리스트가 남은 경우
            a[i:] = right[idxr:]
        return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    A = merge_sort(A)
    print('#{} {} {}'.format(tc, A[N//2], cnt))