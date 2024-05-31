# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        num = nums[0]
        for i in range(1, len(nums)):
            num ^= nums[i]
        
        nums = set(nums)
        
        for num1 in nums:
            for num2 in nums:
                if num1 ^ num2 == num:
                    return [num1, num2]

