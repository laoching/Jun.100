n = []
for i in range(5):
    n.append(input())
for j in range(15):
    for k in range(5):
        if n[j][i] == False:
            continue
        else:
            print(n[k][j], end='')