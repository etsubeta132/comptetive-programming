t = int(input())

for _ in range(t):
    n, z = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    res = 0

    for i, num in enumerate(nums):

        ai = num | z
        res = max(ai, res)
    
    print(res)
        



