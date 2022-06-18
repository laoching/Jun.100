while 1:
    a = int(input().split())
    a = list(a)
    if a[0] == '0':
        exit()
    print(a)
    print(f"{''.join(a)} $")