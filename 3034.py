t, a, b = map(int, input().split())
for i in range(t):
    match = int(input())
    if match <= a or match <= b or match <= ((a ** 2 + b ** 2) ** 0.5):
        print('DA')
    else:
        print('NE')