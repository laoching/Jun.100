a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
tmp = 0

if a > 0:
    print((b - a) * e)
elif a < 0:
    tmp = (a * -1) * c
    tmp = tmp + d + ((b) * e)
    print(tmp)
elif a == 0:
    print(((b - a) * e) + d)