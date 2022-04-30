n, k = map(int, input().split())
N = K = 1
for i in range(n, n-k, -1):
    N *= i
for i in range(1, k+1):
    K *= i
print(N//K)
