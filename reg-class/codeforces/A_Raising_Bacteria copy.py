num = int(input())

ctr = 0
while num:
    num &= num - 1
    ctr+=1

print(ctr)