n = input()
n = n.split(' ')
length = len(n)
for i in n:
    if len(i) == 0:
        length -= 1
print(length)