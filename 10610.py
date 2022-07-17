# 30의 배수가 되는 조건
# 1. 일의 자리가 0이다.
# 2. 각 자리의 숫자들을 더했을 때 3으로 나누어 떨어져야 한다.

n = list(input())
n.sort(reverse = True)
result = 0

for i in n:
    result += int(i)

if result % 3 != 0 or '0' not in n:
    print(-1)
else:
    print(''.join(n))