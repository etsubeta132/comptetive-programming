# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A


def almostPrime(n):
    d = 2
    fact = set()
    while d*d <= n:
        while n % d == 0:
            fact.add(d)
            n //= d
        d+=1
    if n > 1:
        fact.add(n)
 
    if len(fact) == 2:
        return True
    return False

n = int(input())
ctr = 0
for i in range(2,n+1):
    if almostPrime(i):
        ctr+=1
print(ctr)
        
            