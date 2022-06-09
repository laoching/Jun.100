while 1:
    name, age, weight = input().split()
    if name == '#' and age == '0' and weight == '0':
        exit()
    else:
        if int(age) > 17 or int(weight) >= 80:
            print(name + ' Senior')
        else:
            print(name + ' Junior')