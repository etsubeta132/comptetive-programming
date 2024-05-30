
t = int(input())

for _ in range(t):
    n = int(input())
    if n % 2 != 0:
        ans = [i for i in range(1, n+1)]
        ans = ans[::-1]
        ans[0], ans[n//2] = ans[n//2], ans[0]
    else:
        ans = [i for i in range(1, n+1)]
        ans = ans[::-1]
    
    print(*ans)

