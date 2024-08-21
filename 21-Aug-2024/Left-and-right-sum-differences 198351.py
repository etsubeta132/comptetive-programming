# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:


        if len(nums) <=1:
            return [0]
        
        leftSum = [0,nums[0]]
        rightSum = [0]*len(nums)
        rightSum[len(nums)-1] = 0
        rightSum[len(nums)-2] = nums[len(nums)-1]

        diff = []

        for i in range(2,len(nums)):
            leftSum.append(leftSum[i-1]+ nums[i-1])

        for i in range(len(nums)-3,-1,-1):
            rightSum[i] = rightSum[i+1]+nums[i+1]

        for i in range(len(nums)):
            diff.append(abs(rightSum[i] - leftSum[i]))

        return diff
        
            