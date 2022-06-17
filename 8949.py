a, b = input().split()
a = list(a)
b = list(b)
res = []
if len(a) > len(b):
    while 1:
        b.insert(0, '0')
        if len(a) == len(b):
            break
elif len(a) < len(b):
    while 1:
        a.insert(0, '0')
        if len(a) == len(b):
            break    
for i in range(len(a)):
    res.append(int(a[i]) + int(b[i]))
print(*res, sep = '')
