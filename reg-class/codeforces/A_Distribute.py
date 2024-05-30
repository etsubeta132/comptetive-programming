n = int(input())
nums  = list(map(int, input().split()))
nums = [(nums[i], i) for i in range(n)]
nums.sort()

l = 0
r = n - 1
g = 0
while l < r:
    print(nums[l][1] + 1, nums[r][1] + 1)
    l += 1
    r -= 1



