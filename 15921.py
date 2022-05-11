t = int(input())
if t == 0:
    print("divide by zero")
    exit()
n = list(map(int, input().split()))
gi = 0
nSet = set(n)
nSet = list(nSet)
avg = sum(n) / len(n)
for i in range(len(nSet)):
    gi += nSet[i] * (n.count(nSet[i]) / len(n))
if gi == 0:
    print("divide by zero")
else:
    print(f'{avg / gi:.2f}')
    