import sys
input = sys.stdin.readline
n = int(input())
a = set(map(int, input().split())) # set을 써서 중복을 다 죽임 -> list보다 탐색 시간이 더 빠름
n1 = int(input())
b = list(map(int, input().split()))
for i in b:
    if i in a:
        print(1)
    else:
        print(0)