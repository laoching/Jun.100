t = int(input())
li = []
can = []
for i in range(t):
    name = input()
    #아스키 a=97 ~ z=122, 알파벳 개수 = 26
    li.append(ord(name[0]))
li = sorted(li)
sli = set(li)
sli = list(sli)
for j in range(len(sli)):
    if li.count(sli[j]) > 4:
        can.append(sli[j])
can = set(can)
can = list(can)
if len(can) == 0:
    print('PREDAJA')
else:
    for k in range(len(can)):
        print(chr(can[k]), end='')