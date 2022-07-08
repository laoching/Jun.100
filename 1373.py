"""
n = input()
n = n[::-1]
cnt = 0
result = 0
for i in n:
    result += (int(i) * (2 ** cnt))
    cnt += 1
print('{0:o}'.format(result))
"""
n = int(input(), 2)
print(oct(n)[2:])
print('{0:o}'.format(n))