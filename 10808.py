n = input()
li = [0] * 26

for i in n:
    li[ord(i) - 97] += 1
print(*n)