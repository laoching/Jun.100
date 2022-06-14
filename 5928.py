d, h, m = map(int, input().split())
tmp = (11 * 60 + 11)
print((d - 11) * 24 * 60 + (h * 60 + m) - tmp)