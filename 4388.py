while 1:
    a, b = input().split()
    cnt = 0
    carry = 0
    if a == b == '0':
        exit()
    else:
        a = list(a)
        b = list(b)
        for i in range(10 -len(a)):
            a.insert(0, 0)
        for j in range(10 - len(b)):
            b.insert(0, 0)
        for k in range(9, -1, -1):
            if int(a[k]) + int(b[k]) + carry >= 10:
                cnt += 1
                carry = 1
    print(cnt)