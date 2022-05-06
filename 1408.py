nh, nm, ns = map(int,input().split(':'))
sh, sm, ss = map(int,input().split(':'))
if calc < 0:
    calc = (sh * 3600 + sm * 60 + ss) - (nh * 3600 + nm * 60 + ns)
ch = calc // 3600
cm = (calc % 3600) // 60
cs = calc % 60
print("%02d:%02d:%02d" % (ch, cm, cs))