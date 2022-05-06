t = int(input())
n = list(input().split())

priCnt = 0
for i in n:
    if i == '1':
        n.remove(i)
for i in n:
    cnt = 0
    for j in range(2,int(i)):
        if int(i) % j == 0:
            cnt += 1
    if cnt == 0:
        priCnt += 1
print(priCnt)