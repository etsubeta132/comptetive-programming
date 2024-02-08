class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        prefixSum = [0]*n
        prefixSum[0] = nums[0]
        result = [0]*n
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        
        suffixSum = [0]*n
        suffixSum[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffixSum[i] = suffixSum[i+1] + nums[i]
        

        
        for i in range(n):
            before = abs((prefixSum[i]-nums[i]) - nums[i]*i)
            after = abs((suffixSum[i]-nums[i]) - nums[i]*(n-i-1))
            result[i] = before + after
        
        return result

        
        
