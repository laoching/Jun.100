t = int(input())
alpha = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
alpha_dick = {}
cnt_alpha = 1
for _ in alpha:
    alpha_dick[_] = cnt_alpha
    cnt_alpha += 1
for i in range(t):
    
    cnt_rule = 1
    cnt_plain = 1
    match_rule = {}
    match_plain = []
    result = []

    plain = input()
    rule = input()

    for j in plain:
        plain_index = alpha_dick.get(j)
        match_plain.append(plain_index)

    for i in rule:
        match_rule[cnt_rule] = i
        cnt_rule += 1
    
    for k in match_plain:
        crypto = match_rule.get(k)
        if crypto is None:
            crypto = ' '
        result.append(crypto)

    print(''.join(result))