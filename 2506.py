import sys
t = int(sys.stdin.readline())
cnt = 0
chain = 0
li = list(map(int, sys.stdin.readline().split()))
for i in range(len(li)):
    if li[i] == 1:
        cnt += 1
        chain += cnt
    else:
        cnt = 0
print(chain)