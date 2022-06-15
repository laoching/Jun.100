li = []
cnt = {}
rrr = []
for i in range(int(input())):
    li.append(input())
li = sorted(li)
lise = set(li)
lise = list(lise)
lise = sorted(lise, reverse=True)
for i in range(len(lise)):
    rrr.append(li.count(lise[i]))
    cnt[li.count(lise[i])] = lise[i]

print(cnt.get(max(rrr)))
