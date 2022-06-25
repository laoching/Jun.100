while 1:
    n = list(input())
    if n == 'END':
        exit()
    for i in range(len(n) - 1, -1, -1):
        print(n[i], end = '')
        print()