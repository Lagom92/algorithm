T = int(input())
for tc in range(1, T+1):
    n2 = input()
    n3 = input()

    a = n2
    b = list(a)  # 2진수에 숫자를 하나씩 변환
    res = []
    for i in range(len(b)):
        if b[i] == '0':
            b[i] = '1'
        else:
            b[i] = '0'
        res.append(''.join(b))
        b = list(a)

    result = []    # 2진수를 10진수로 바꿔서 result에 넣음
    for i in range(len(res)):
        result.append(int(res[i], 2))

    # print(result)

    a = n3
    b = list(a)  # 3진수에 숫자를 하나씩 변환
    res = []
    for i in range(len(b)):
        if b[i] == '2':
            b[i] = '1'
            res.append(''.join(b))
            b[i] = '0'

        elif b[i] == '1':
            b[i] = '2'
            res.append(''.join(b))
            b[i] = '0'

        else:
            b[i] = '1'
            res.append(''.join(b))
            b[i] = '2'

        res.append(''.join(b))
        b = list(a)
    # print(res)
    for i in range(len(res)):
        if int(res[i], 3) in result:
            print('#{} {}'.format(tc, int(res[i], 3)))

