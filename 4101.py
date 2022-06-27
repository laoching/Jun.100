while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        exit()
    else:
        if a > b:
            print('YES')
        else:
            print('NO')