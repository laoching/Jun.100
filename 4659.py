mo = 'aeiou'

while 1:
    pw = input()
    if pw == "end":
        exit()
    mocnt = 0
    morepeat = 0
    jarepeat = 0
    result = 0
    tmp = ''

    for i in pw:
        if i in mo:
            jarepeat = 0
            mocnt += 1
            morepeat += 1
            if morepeat >= 3:
                result += 1
            if tmp == i:
                if i == 'e' or i == 'o':
                    pass
                else:
                    result += 1
        else:
            morepeat = 0
            jarepeat += 1
            if jarepeat >= 3:
                result += 1
            if tmp == i:
                result += 1
        tmp = i
    
    if mocnt < 1:
        result += 1
    
    if result == 0:
        print(f'<{pw}> is acceatable.')
    else:
        print(f'<{pw}> is not acceptable.')