t = int(input())
ball = 1
for i in range(t):
    a, n = map(int, input().split())
    if ball == a:
        ball = n
    elif ball == n:
        ball = a
print(ball)
