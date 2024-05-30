import math, sys


def solve():
    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    if a.count(a[0]) == n:
        return 0

    for x in a:
        if (x >= k and a[0] <= k) or (x <= k and a[0] >= k):
            return -1
    gcd = abs(k - a[0])

    for i in a:
   	    gcd = math.gcd(gcd, abs(k - i))
    
    ans = 0
    for i in a:
   	    ans += (abs(k - i) // gcd - 1)
    
    return ans

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
   	    print(solve())