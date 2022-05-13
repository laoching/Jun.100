import sys
a, n = map(int, sys.stdin.readline().split())
a -= 1
n -= 1
aCol = (a // 4)
aRow = (a % 4)
nCol = (n // 4)
nRow = (n % 4)

if aCol != 0:
    aCol += 1
if aRow == 0:
    aRow = 4
if nCol != 0:
    nCol += 1
if nRow == 0:
    nRow = 4
ans = abs(aCol - nCol) + abs(aRow - nRow)
print(ans)