import sys
start = int(sys.stdin.readline())
end = int(sys.stdin.readline())
result = []
for i in range(start, end + 1):
    cnt = 0
    if i > 0:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            result.append(i)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))