while 1:
    a, b = map(int, input().split())
    result = 0
    result += a
    while a // b:
        result += a // b
        a = a // b + a % b
    print(result)
