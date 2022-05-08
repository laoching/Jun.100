a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
xTotal = a * p
if p <= c:
    yTotal = b
else:
    yTotal = b + ((p - c) * d)
if xTotal < yTotal:
    print(xTotal)
else:
    print(yTotal)