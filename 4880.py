while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        exit()
    elif c - b == b - a:
        print('AP', c + (b - a))
    elif b // a == c // b:
        print('GP', c * (b // a))