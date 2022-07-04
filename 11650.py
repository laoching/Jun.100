li = []
for i in range(int(input())):
    li.append(list(map(int, input().split())))
li = sorted(li)
for i in li:
    print(i[0], i[1])
