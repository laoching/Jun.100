import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b, c, d, e = map(int, sys.stdin.readline().split())
    result = (a * 350.34) + (b * 230.90) + (c * 190.55) + (d * 125.30) + (e * 180.90)
    print(f'${result:.2f}')
