
n = int(input())
probability = list(map(float, input().split()))

dp = [[0]*(n + 1) for j in range(n + 1)]

for i in range((n // 2) + 1, n + 1):
    dp[i][-1] = 1

for i in range(n):
    dp[-1][1] = 1


for ctr in range(n - 1, -1, -1):
    for idx in range(n - 1, -1, -1):

        head = probability[idx] * dp[ctr + 1][idx + 1]
        tail = (1 - probability[idx]) * dp[ctr][idx + 1]
        
        dp[ctr][idx] = head + tail

print(dp[0][0])
# def dp(ctr, idx):

#     if idx == n:
#         if ctr > (n // 2):
#             return 1
#         return 0
    
#     head = probability[idx] * dp(ctr + 1, idx + 1)
#     tail = (1 - probability[idx]) * dp(ctr, idx + 1)
    
#     return head + tail

# print(dp(0, 0))
    
        
