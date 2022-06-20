for i in range(int(input())):
    n = list(map(int, input().split()))
    n = sorted(n)
    n.pop(0)
    n.pop()
    if max(n) - min(n) >= 4:
        print("KIN")
    else:
        print(sum(n))