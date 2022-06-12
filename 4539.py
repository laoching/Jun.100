for i in range(int(input())):
    n = input()
    a = n
    nlen = len(n)
    result = int(n) / int('1' + '0' * (nlen - 1)) * int('1' + '0' * (nlen - 2))
    while 1:
        resulta = round(result + 0.000000001)
        if resulta / 10 == 1:
            break
        if len(str(resulta)) == 1:
            break
        result = resulta / int('1' + '0' * (nlen - 1)) * int('1' + '0' * (nlen - 2))
    print(resulta * int('1' + '0' * (nlen - 1)))