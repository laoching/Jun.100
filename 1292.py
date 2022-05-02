total = 0
cnt = 0
nuLi = []
n, k = map(int, input().split())
while 1:
    if cnt == k:
        break
    else:
        cnt += 1
    for i in range(cnt):
        nuLi.append(cnt)
    
print(nuLi)
for j in range(n - 1, k):
    total += nuLi[j]
print(total)
