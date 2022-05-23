nuLi = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        nuLi.append(n)
if len(nuLi) > 0:
    print(sum(nuLi))
    print(min(nuLi))
else:
    print(-1)
