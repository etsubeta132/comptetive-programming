n = int(input())
chars = input()

ctr = 0
cur = []
result = []
def dp(idx):
    global ctr

    if idx >= n:
        result.append(cur[:])
        ctr += 1
        return 
    
    for num in range(idx, n + 1):
        cur.append(num)
        dp(idx + 1)
        cur.pop()

print(result)
print(dp(0))

    