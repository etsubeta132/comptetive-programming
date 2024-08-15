# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ctr = 0
        
        while l <= r:
            while l <= r and nums[r] + nums[l] > target:
                r -= 1
            
            if l <= r:
                ctr += 2**(r - l)
            l += 1
        
        return ctr % (10**9 + 7)
        