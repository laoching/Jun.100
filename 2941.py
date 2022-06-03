cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 's=', 'z=']
n = input()

for i in cro:
    n = n.replace(i, '1')
print(len(n))