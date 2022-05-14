'''
# ---- 시 간 초 과 ----
import sys
result = []
stu, time = map(int, sys.stdin.readline().split())
for i in range(stu):
    t = int(sys.stdin.readline())
    for j in range(time):
        if j % t == 0:
            result.append(j)
print(len(set(result)))
'''
'''
# ---- 메 모 리 초 과 ----
import sys
stu, time = map(int, sys.stdin.readline().split())
result = []
for i in range(stu):
    t = int(sys.stdin.readline())
    for j in range(t, time + 1, t):
        result.append(j)
print(len(set(result)))
'''
'''
# ---- 시 간 초 과 ----
import sys
stu, time = map(int, sys.stdin.readline().split())
result = [False] * (time + 1)
cnt = 0
for i in range(stu):
    t = int(sys.stdin.readline())
    for j in range(t, time + 1, t):
        if not result[j]:
            result[j] = True
            cnt += 1
print(cnt)
'''