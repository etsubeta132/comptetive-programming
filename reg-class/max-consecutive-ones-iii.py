class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        r ,l = 0 , 0
        res = 0
        while r < len(nums):
            if nums[r]==0:
                k-=1
            while k < 0:
                if nums[l]==0:
                    k+=1
                l+=1
            res = max(res,r-l+1)
            r += 1
        return res

