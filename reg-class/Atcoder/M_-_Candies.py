N, candies = map(int, input().split())
max_candy = list(map(int, input().split()))

MOD = (10**9) + 7


dp = [[0] * (candies + 1) for _ in range(N + 1)]

dp[0][0] = 1
 
for idx in range(1, N + 1):
    for candy in range(candies + 1):
        dp[idx][candy] = dp[idx - 1][candy]

        if candy > 0:
            dp[idx][candy] += dp[idx][candy - 1]

            if candy > max_candy[idx - 1]:
                dp[idx][candy] -= dp[idx - 1][candy - max_candy[idx - 1] - 1]
        
    dp[idx][candy] = dp[idx][candy] % MOD

print(dp[N][candy])
