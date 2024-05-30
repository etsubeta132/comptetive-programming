item_len, weight = map(int, input().split())
items = []

for _ in range(item_len):
    item = tuple(map(int, input().split()))
    items.append(item)

dp = [[0]*(item_len + 1) for _ in range(weight + 1)]

for idx in range(item_len - 1, -1, -1):
    w, val = items[idx]

    for wt in range(weight + 1):
        take = nottake = 0
        take = 0
        if wt - w >= 0:
            take = val + dp[wt - w][idx + 1]
            
        nottake = dp[wt][idx + 1]
        
        dp[wt][idx] = max(take, nottake)

print(dp[-1][0])
    