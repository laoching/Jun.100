cnt = 0
fac = 1
res = 1
print(f'n e')
print(f'- -----------')
print(f'{cnt} {res}')

for i in range(1, 10):
    cnt += 1
    fac *= 1 / i
    res += fac
    if cnt == 1:
        print(f'{cnt} {int(res)}')
    elif cnt == 2:
        print(f'{cnt} {res:.1f}')
    else:
        print(f'{cnt} {res:.9f}')
    