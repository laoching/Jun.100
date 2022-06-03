plain = set(range(1, 10000))
notself = set()
for i in plain:
    for j in str(i):
        i += int(j)
    notself.add(i)
self = sorted(plain - notself)
for k in self:
    print(k)
