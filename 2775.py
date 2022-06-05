t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())

    zero = [j for j in range(1, n + 1)]
    for floor in range(k):
        for ho in range(1, n):
            zero[ho] += zero[ho - 1]
    print(zero[-1])
