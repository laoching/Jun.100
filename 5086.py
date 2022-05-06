while 1:
    a, b = map(int,input().split())
    cnt = 0
    if a > b:
        if a % b == 0:
            print('multiple')
        else:
            cnt += 1
    elif a < b:
        if b % a == 0:
            print('factor')
        else:
            cnt += 1
    if cnt > 0:
        print('neither')
    if a == 0 and b == 0:
        break
'''
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
'''