n = list(map(int, input().split()))
a = sorted(n)
d = sorted(n,reverse=True)
if a == n:
    print('ascending')
elif d == n:
    print('descending')
else:
    print('mixed')
