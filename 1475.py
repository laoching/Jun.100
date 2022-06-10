n = input()
li = [0] * 10
for i in range(len(n)):
    if int(n[i]) == 6 or int(n[i]) == 9:
        if li[6] > li[9]:
            li[9] += 1
        else:
            li[6] += 1
    else:
        li[int(n[i])] += 1
print(max(li))