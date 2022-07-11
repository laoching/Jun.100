n, m = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
a = 0

while a == n:
    res = 0
    for i in range(a, n):
        res += li[i]
        if res == n:
            cnt += 1
            break
    a += 1
print(cnt)