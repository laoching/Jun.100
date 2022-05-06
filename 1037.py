real_cnt = int(input())
if real_cnt == 1:
    real_num = int(input())
    print(real_num**2)
else:
    real_num = list(map(int, input().split()))
    real_num.sort()
    sum = real_num[0] * real_num[-1]
    print(sum)