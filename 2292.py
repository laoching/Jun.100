cnt = 1
distance = 1
n = int(input())
while n > distance:
    distance += 6 * cnt
    cnt += 1
print(cnt)