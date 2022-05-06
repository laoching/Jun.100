t = int(input())
nL = []
for i in range(t):
    n = int(input())
    if n == 0:
        nL.pop()
    else:
        nL.append(n)
print(sum(nL))
