t = int(input())

for _ in range(t):
    n, m, k = list(map(int, input().split()))
    dp =[[0]* m for _ in range(n)]
    
    for i in range(n):
        dp[i][0] = i

    for i in range(m):
        dp[0][i] = i
    
    for i in range(1, n):
        for j in range(1, m):
            right = down = float("inf")
            if j - 1 >= 0:
                right = i + 1 + dp[i][j - 1]
            if i - 1 >= 0:
                down = j + 1 + dp[i - 1][j]
            dp[i][j] = min(right, down)

    print("YES" if dp[-1][-1] == k else "NO")


    
    





