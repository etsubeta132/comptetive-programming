# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        target_list = []
        for i in nums:
            if i == target:
                target_list.append(nums.index(i))
                nums[nums.index(i)] = " "
        return target_list