N, m, M, T, R = map(int, input().split())
exc = 0
rest = 0
mac = m
if (m + T) > N:
    print(-1)
    exit()
while 1:
    if (mac + T) <= M:
        mac += T
        exc += 1
    else:
        mac -= R
        if mac < m:
            mac = m
        rest += 1
    if exc == N:
        print(exc + rest)
        exit()
    