tnum = int(input())
for i in range(tnum):
    a,b = map(int, input().split())
    c=1
    d=1
    for i in range(0,a):
        c *= (a-i)
        d *= (b-i)
    print(d//c)