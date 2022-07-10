import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
n1 = int(input())
b = list(map(int, input().split()))
for i in b:
    if i in a:
        print(1)
    else:
        print(0)