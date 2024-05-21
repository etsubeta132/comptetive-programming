n, w = map(int, input().split())
path = []

for _ in range(n):
    row = list(input())
    path.append(row)

dp = [[0]*w  for _ in range(n)]
dp[0][0] = 1

for i in range(1, n):
    if path[i][0] == ".":
        dp[i][0] = dp[i - 1][0]
    else:
        dp[i][0] = 0

for i in range(1, w):
    if path[0][i] == ".":
        dp[0][i] = dp[0][i - 1]
    else:
        dp[0][i] = 0


for i in range(1, n):
    for j in range(1, w):
        if path[i][j] != "#":
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


print(dp[-1][-1] % ((10 ** 9) + 7))


   
