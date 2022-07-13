import sys
for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    for cnt in range(1, a * b + 1):
        if (b * cnt) % a == 0:
            print(cnt * b)
            break
