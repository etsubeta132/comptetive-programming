class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)):
            if mx < i:
                return False 
            mx = max(mx,nums[i]+i)
            
        return True