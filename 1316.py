t = int(input())
cnt = 0
group = 0
for i in range(t):
    n = list(input())
    for j in range(len(n) - 1):
        if n[j] != n[j + 1]:
            new = n[j + 1:]
            if new.count(n[j]) > 0:
                cnt += 1
    if cnt == 0:
        group += 1
print(group)
