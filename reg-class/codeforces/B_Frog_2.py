

def dp(n, k, arr):
    dp = [0] * n

    dp[0] = 0
    for i in range(1, n):
        res = float("inf")
        j = 1

        while j <= k and i - j >= 0:
            res = min(res, dp[i - j] + abs(arr[i] - arr[i - j]))
            j += 1

        dp[i] = res

    return dp[n - 1]

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(dp(n, k, arr))