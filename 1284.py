while 1:
    n = input()
    sum = 0
    if n == '0':
        exit()
    for i in n:
        if i == '0':
            sum += 4
        elif i == '1':
            sum += 2
        else:
            sum += 3
    print(sum + 2 + len(n)-1)