import sys
for i in range(3):
    t = int(sys.stdin.readline())
    for j in range(t):
        sum = 0
        n = int(sys.stdin.readline())
        n = long(n)
        sum += n
    if sum == 0:
        print(0)
    elif sum > 0:
        print('+')
    else:
        print('-')