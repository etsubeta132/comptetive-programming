class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixSum = [0]
        n = len(nums)
        for i in range(1, n + 1):
            prefixSum.append(nums[i - 1] + prefixSum[i - 1])
        m_Index = None
        for i in range(n - 1, -1, -1):
            back_sum = prefixSum[-1] - prefixSum[i+1]
            if prefixSum[i] == back_sum:
                m_Index = i
        if m_Index is None:
            return -1
        else:
            return m_Index