t = int(input())
alpha = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
alpha_dick = {}
cnt_alpha = 1
for _ in alpha:
    alpha_dick[_] = cnt_alpha
    cnt_alpha += 1
for i in range(t):
    
    cnt_rule = 1
    cnt_cypertext = 1
    match_rule = {}
    match_cypertext = []
    result = []

    cypertext = input()
    rule = input()

    for j in cypertext:
        cypertext_index = alpha_dick.get(j)
        match_cypertext.append(cypertext_index)

    for i in rule:
        match_rule[cnt_rule] = i
        cnt_rule += 1
    
    for k in match_cypertext:
        crypto = match_rule.get(k)
        if crypto is None:
            crypto = ' '
        result.append(crypto)

    print(''.join(result))

"""
for i in cypertext:
    if i == ' ':
        print(' ', end = "")
    else:
        print(key[ord(i) - ord("A")], end="")
"""