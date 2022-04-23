val = []
mul = 0
r = {'black' : [0, 1], 'brown' : [1, 10], 'red' : [2, 100], 'orange' : [3, 1000], 'yellow' : [4, 10000],
     'green' : [5, 100000], 'blue' : [6, 1000000], 'violet' : [7, 10000000], 'grey' : [8, 100000000],
     'white' : [9, 1000000000]}
for i in range(3):
     color = input()
     val.append(r[color][0])
     if i == 2:
          mul = r[color][1]
print(f'{(val[0] * 10 + val[1]) * mul}')

'''
color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
f = color.index(input())
s = color.index(input())
t = color.index(input())
r = int(str(f) + str(s)) * (10 ** t)
print(r)
'''