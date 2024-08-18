# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i
        
        
        if len(nums) >= 2 and nums[-1] > nums[-2]:
            return len(nums) - 1
        
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
          

        