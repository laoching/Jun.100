t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        if j == 0:
            print('#' * n)
        elif j != 0 and j != (n - 1):
            print('#' + 'J' * (n - 2) + '#')
        else:
            print('#' * n)
    print()