# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        n -= n%10
        while n%7:
            n += 1
        print(n)