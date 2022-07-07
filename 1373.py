import sys
n = sys.stdin.readline()
n = n[::-1]
cnt = 0
result = 0
for i in n:
    result += (int(i) * (2 ** cnt))
    cnt += 1
print('{0:o}'.format(result))
