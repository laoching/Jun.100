import sys
cnt = -1
nu = []
while 1:
    n = float(sys.stdin.readline())
    if n == 999:
        exit()
    nu.append(n)
    cnt += 1
    if cnt > 0:
        print(f'{nu[cnt] - nu[cnt - 1]:.2f}')