n = int(input())
da = int(input())
candi = []
cnt = 0
for i in range(n - 1):
    candi.append(int(input()))

if len(candi) > 0:
    while max(candi) >= da:
        elec = candi.index(max(candi))
        candi[elec] -= 1
        da += 1
        cnt += 1
print(cnt)