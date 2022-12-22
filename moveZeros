class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index1 = 0
        index2 = len(nums) - 1
        while index1 < index2:
            if nums[index1] == 0:
                nums.remove(0)
                nums.append(0)
                index2 -= 1
            else:
                index1 +=1
        return nums
