# Problem: Can I Square? - https://codeforces.com/contest/1915/problem/C

import math

t = int(input())

for _ in range(t):
    x = int(input())
    nums = [int(i) for i in input().split()]
    
    total = sum(nums)
    x = int(math.sqrt(total))
    
    if math.pow(x, 2) == total:
        print("YES")
    else:
        print("NO")