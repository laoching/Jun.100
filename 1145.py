word = list(input().upper())
clean_list = list(set(word))
cnt = []

for i in clean_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(clean_list[(cnt.index(max(cnt)))])

