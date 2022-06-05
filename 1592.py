n, m, l = map(int, input().split())
li = [1]
cnt = 0
pnt = 0
for i in range(n - 1):
    li.append(0)
# -1이 마지막 인자, -2가 뒤에서 두번째
while 1:
    if max(li) == m:
        print(cnt)
        exit()
    else:
        cnt += 1
        if li[pnt % n] % 2 == 0:
            pnt -= l
            li[pnt % n] += 1
        else:
            pnt += l
            li[pnt % n] += 1
    
    