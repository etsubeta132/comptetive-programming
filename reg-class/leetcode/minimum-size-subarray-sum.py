class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l,r = 0,0
        res = 0
        window = len(nums)+1

        while r < len(nums):
            res+=nums[r]
            r+=1
            while res >= target:
                window = min(window,r-l)
                res-=nums[l]
                l+=1
            
        if window == len(nums)+1:
            return 0
        else:
            return window
            
        



            
        