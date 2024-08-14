# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums = []
        negative_nums = []
        rearanged_nums =[]
        for num in nums:
            if num>=0:
                positive_nums.append(num)
            else:
                negative_nums.append(num)
        
        for idx in range(len(positive_nums)):
            rearanged_nums.append(positive_nums[idx])
            rearanged_nums.append(negative_nums[idx])
        
        return rearanged_nums