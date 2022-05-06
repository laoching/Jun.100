height = []
nan1 = 0
nan2 = 0
for i in range(9):
    height.append(int(input()))
for i in range(8):
    for j in range(i+1, 9):
        if sum(height) - (height[i] + height[j]) == 100:
            nan1 = height[i]
            nan2 = height[j]
height.remove(nan1)
height.remove(nan2)
height.sort()
for k in range(7):
    print(height[k])
