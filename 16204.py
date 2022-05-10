n, m, k = map(int, input().split())
x1 = x2 = o1 = o2 = 0
o1 = m
x1 = n - m
o2 = k
x2 = n - k
result = 0

if x1 < x2:
    result += x1
else:
    result += x2
if o1 < o2:
    result += o1
else:
    result += o2
print(result)