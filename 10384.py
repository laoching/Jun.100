t = int(input())
for i in range(1, t + 1):
    cnt = 0
    case = input()
    case = case.lower()
    alphabetList = [0] * 26
    for j in case:
        if j.isalpha():
            alphabetList[ord(j) - 97] += 1
    if min(alphabetList) >= 3:
        print(f'Case {i}: Triple pangram!!!')
    elif min(alphabetList) >= 2:
        print(f'Case {i}: Double pangram!!')
    elif min(alphabetList) >= 1:
        print(f'Case {i}: Pangram!')
    else:
        print(f'Case {i}: Not a pangram')
