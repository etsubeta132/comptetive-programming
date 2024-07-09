# Problem: Honest Coach - https://codeforces.com/problemset/problem/1360/B

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    ans = float("inf")

    for i in range(1, n):
        ans = min(ans, nums[i] - nums[i - 1])

    print(ans)
