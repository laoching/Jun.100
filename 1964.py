n = int(input())
five = 5
result = five
if n == 1:
    print(five)
else:
    for i in range(2, n + 1):
        result += ((i * 3) + 1)
    print(result)