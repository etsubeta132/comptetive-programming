class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l,r = 0,0
        win = 0
        ones = 0
        while r<len(nums):
            ln = r-l+1
            if nums[r] == 1:
                ones+=1
            win = max(win,ones)
            while l< r and ln - ones > 1:
                if nums[l] == 1:
                    ones-=1
                l+=1
                ln = r-l+1
            r+=1
        if win == len(nums):
            return win-1
        return win



            


