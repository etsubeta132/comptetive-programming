n, m, k = list(map(int, input().split()))

potl_frs = []
for i in range(1, m+1):
    fr = int(input())
    potl_frs.append(fr)

fedor = int(input())

friends = 0
for fr in potl_frs:
    xor = fr ^ fedor
    ctr = 0
    while xor:
        xor &= (xor - 1)
        ctr += 1
    
    if ctr <= k:
        friends += 1

print(friends)




