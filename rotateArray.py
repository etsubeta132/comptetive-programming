class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        while len(nums) < k:
            k = k - len(nums)
        right = len(nums) - k
        newList = []
        if len(nums) != k:
            while left < (len(nums) - k):
                if right < len(nums):
                    newList.append(nums[right])
                    right += 1
                else:
                    newList.append(nums[left])
                    left += 1
            for i in range(len(nums)):
                nums[i] = newList[i]
