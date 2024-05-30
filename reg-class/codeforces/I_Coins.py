n = int(input())
probability = list(map(float, input().split()))
ans = [0]

def dp(idx, ctr):

    if idx >= n:
        return 1
    
    return probability[idx] * dp(idx + 1, ctr + 1)
dp(0, 0)
print(ans)