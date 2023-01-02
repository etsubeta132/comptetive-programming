class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_of_opp = 0
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            result = nums[left] + nums[right]
            if result > k:
                right -= 1
            elif result < k:
                left += 1
            else:
                num_of_opp += 1
                right -= 1
                left += 1
        return num_of_opp
