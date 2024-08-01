# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        mn = 1
        l = len(nums) - 2
        while l > 0:
            if nums[l] >= mn:
                mn = 1
            else:
                mn += 1
            l -= 1
        
        if nums[l] >=  mn:
            return True
        else:
            return False
        
        
        



            
