class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ctr = 0
        max_ctr = 0
        for i in nums:
            if i==1:
                ctr+=1
            elif i==0:
                max_ctr = max(max_ctr,ctr)
                ctr=0
        max_ctr = max(max_ctr,ctr)
        return max_ctr