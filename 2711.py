for i in range(int(input())):
    n = input()
    loca = int(n[0])
    text = list(n[2:])
    text.pop(loca - 1)
    print(''.join(text))