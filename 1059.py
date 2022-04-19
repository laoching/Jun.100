num = int(input())
word_list = []

for i in range(num):
    word = input()
    word_list.append(word)
word_list = set(word_list)
word_list = list(word_list)
word_list.sort()
word_list.sort(key=len)

for i in word_list:
    print(i)