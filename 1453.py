t = int(input())
n = list(map(int, input().split()))
cleanN = set(n)
print(len(n) - len(cleanN))
