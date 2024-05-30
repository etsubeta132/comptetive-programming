from collections import defaultdict
item_len, weight = map(int, input().split())
items = []
total = 0
tot_weight = 0

for _ in range(item_len):
    item = tuple(map(int, input().split()))
    total += item[1]
    tot_weight += item[0]

    items.append(item)


memo = defaultdict(inf)
def dp(i, value, weight):
    state = (i, value)
    if state  not in memo:
        pick = dp(i - 1, value-items[i][1], weight - items[i][0])
        not_pick = dp(i-1, value, weight)

        memo[state] = min(pick, not_pick)
    
    return memo[state]

print(dp(item_len-1, total, tot_weight))
