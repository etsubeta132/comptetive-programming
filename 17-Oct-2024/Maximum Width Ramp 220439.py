# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:


        num_idx = [i for i in range(len(nums))]

        num_idx.sort(key=lambda i: (nums[i], i))

        idx = len(nums) 
        width = 0

        for i in num_idx:
            width = max(width, i - idx)
            idx = min(idx, i)

        return width