cnt = 0
cntb = 0
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a > b:
        cnt += 1
    elif a == b:
        pass
    else:
        cntb += 1
print(cnt, cntb)