result = int(input())
price = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    price += a * b
if price == result:
    print('Yes')
else:
    print('No')	