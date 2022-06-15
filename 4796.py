cnt =0
while 1:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        exit()
    cnt += 1
    print(f'Case {cnt}: {l * (v // p) + v - ((v // p) * p)}')