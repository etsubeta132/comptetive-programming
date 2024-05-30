# n, w = map(int, input().split())
# path = []

# for _ in range(n):
#     row = list(input())
#     path.append(row)

# memo = {}
# def dp(r, c):
#     if r < 0 or r >= n or c < 0 or c >= w:
#         return 0
    
#     if r == n - 1 and c == w - 1:
#         return 1
    
#     if path[r][c] == "#":
#         return 0
    
#     if (r, c) not in memo:
#         memo[(r,c)] = dp(r, c + 1) + dp(r + 1, c)

#     return memo[(r, c)]

# val = dp(0,0)
# print(val)

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


   