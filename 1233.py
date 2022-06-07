a, b, c = map(int, input().split())
fre = [0 for _ in range(200)]
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            fre[i + j + k] += 1
print(fre.index(max(fre)))