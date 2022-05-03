DAY = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
numOfDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mon, day = map(int, input().split())
k = 0
for i in range(mon - 1):
    k += numOfDay[i]
k = (k + day) % 7
print(DAY[k])