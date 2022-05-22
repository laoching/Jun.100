t = int(input())
print()
for i in range(t):
    candy = 0
    n = int(input())
    for j in range(n):
        candy += int(input())
    if candy % n == 0:
        print("YES")
    else:
        print('NO')
    print(candy)
    print()