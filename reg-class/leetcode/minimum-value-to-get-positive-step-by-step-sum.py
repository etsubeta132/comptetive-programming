class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefSum = [0]*len(nums)
        prefSum[0] = nums[0]

        mn = nums[0]

        for i in range(1,len(nums)):
            prefSum[i] = prefSum[i-1] + nums[i]
            mn = min(mn,prefSum[i])
        
        res = 1 - mn
        
        return res if res > 0 else 1


        

        
        return mn 
        
        