# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ctr = 0
        for i in range(len(nums)-1, -1, -1):
            x = nums[i]
            l = bisect_left(nums, lower - x, 0, i)
            h = bisect_right(nums, upper - x, 0, i)
            ctr += h - l
        return ctr 