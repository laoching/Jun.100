while 1:
    n = input()
    if n == '#':
        break
    mo = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    n = n.lower()
    for i in n:
        if i in mo:
            cnt += 1
    print(cnt)
