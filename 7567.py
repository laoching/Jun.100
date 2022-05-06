dish = input()
cnt = 0
for i in range(len(dish) - 1):
    if dish[i] == dish[i + 1]:
        cnt += 1
print((len(dish) * 10) - (cnt * 5))