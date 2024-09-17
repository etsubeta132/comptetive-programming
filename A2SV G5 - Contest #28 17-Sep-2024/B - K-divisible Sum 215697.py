# Problem: B - K-divisible Sum - https://codeforces.com/gym/540354/problem/B

import math
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    ans = 0
    if n % k == 0:
        ans = (n //  k) * k
    else:
        ans = ((n //  k) + 1) * k
    print(math.ceil(ans / n))
    

    