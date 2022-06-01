a = input()
n = list(a)
mo = ['a', 'e', 'i', 'o', 'u']
for i in range(len(n)):
    if n[i] in mo:
        n[i + 1] = '0'
        n[i + 2] = '0'
for j in range(len(n)):
    if n[j] == '0':
        n[j] = ''
print(''.join(n))