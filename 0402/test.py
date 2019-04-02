def find(b, t):
    # 2진수로 만들 수 있는 숫자를 set으로 저장
    # 각 자리 수는 문자열로 검사
    bstr = str(b)
    bset = set()
    for i in range(len(bstr)):  # 문자열의 길이만큼 자리수
        if (bstr[len(bstr) - i - 1] == '0'):
            bset.add(int(str(b + 10 ** i), 2))
        else:
            bset.add(int(str(b - 10 ** i), 2))
    # 3진수로 만들 수 있는 숫자 set
    tstr = str(t)
    tset = set()
    for i in range(len(tstr)):
        if (tstr[len(tstr) - i - 1] == '0'):
            if (int(str(t + 10 ** i), 3) in bset):
                return int(str(t + 10 ** i), 3)
            if (int(str(t + 2 * 10 ** i), 3) in bset):
                return int(str(t + 2 * 10 ** i), 3)

        elif (tstr[len(tstr) - i - 1] == '1'):
            if ((int(str(t - 10 ** i), 3) in bset)):
                return int(str(t - 10 ** i), 3)
            if (int(str(t + 10 ** i), 3) in bset):
                return int(str(t + 10 ** i), 3)

        elif (tstr[len(tstr) - i - 1] == '2'):
            if (int(str(t - 10 ** i), 3) in bset):
                return int(str(t - 10 ** i), 3)
            if ((int(str(t - 2 * 10 ** i), 3) in bset)):
                return int(str(t - 2 * 10 ** i), 3)

    # return (bset&tset) #교집합 중 한개만 리턴


T = int(input())
for tc in range(1, T + 1):
    b = int(input())
    t = int(input())
    r = str(find(b, t))
    print('#{} {}'.format(tc, r))