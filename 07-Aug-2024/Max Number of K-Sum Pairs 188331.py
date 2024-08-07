# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1
        ctr = 0
        while l < r:
            sm = nums[l] + nums[r]
            if sm == k:
                ctr += 1
                l += 1
                r -= 1
            elif sm > k:
                r -= 1
            else:
                l += 1
        
        return ctr
        

        