while 1:
    n = input()
    gi = n[0]
    text = n[2:].lower()
    cnt = 0
    for i in range(len(text)):
        if text[i] == gi:
            cnt += 1
    print(gi + " " + str(cnt))