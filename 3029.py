a = input()
b = input()
a = list(a)
b = list(b)
ase = int(''.join(a[6:]))
bse = int(''.join(b[6:]))
ami = int(''.join(a[3:5]))
bmi = int(''.join(b[3:5]))
aho = int(''.join(a[:2]))
bho = int(''.join(b[:2]))
if bse - ase < 0:
    second = bse + 60 - ase
    bmi -= 1
else:
    second = bse - ase
if bmi - ami < 0:
    minute = bmi + 60 - ami
    bho -= 1
else:
    minute = bmi - ami
if bho - aho < 0:
    hour = bho + 24 - aho
else:
    hour = bho - aho
print("%02d:%02d:%02d" % (hour, minute, second))