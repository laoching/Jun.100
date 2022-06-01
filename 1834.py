n = int(input())
result = 0
cnt = 0
while 1:
    cnt += 1
    if (cnt // n) == (cnt % n):
        result += cnt
print(cnt) 