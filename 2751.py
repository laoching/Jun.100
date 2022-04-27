import sys

t = int(sys.stdin.readline())
n = []
for i in range(t):
    n.append(int(sys.stdin.readline()))
n.sort()
for i in range(t):
    print(n[i])
