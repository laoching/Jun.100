import sys
while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    lng = []
    lng.append(a)
    lng.append(b)
    lng.append(c)
    lng.sort()
    print(lng)
    if a == b == c == 0:
        exit()
    if lng[2] < (lng[0] + lng[1]): 
        if a == b == c:
            print("Equilateral")
        elif a == b or a == c or b == c:
            print("Isosceles")
        elif a != b != c:
            print("Scalene")
    else:
        print("Invalid")