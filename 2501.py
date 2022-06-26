n, cnt = map(int, input().split())
li = []
try:
    for i in range(1, n + 1):
        if n % i == 0:
            li.append(i)
    print(li[cnt - 1])
except:
    exit()