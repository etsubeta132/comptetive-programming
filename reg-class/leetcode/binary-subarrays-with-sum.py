class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefSum  = {0:1}
        
        curr_sum = 0
        res = 0 

        for i in range(len(nums)):
            curr_sum += nums[i]
            k  = curr_sum - goal
            res+= prefSum.get(k,0)
            prefSum[curr_sum] = prefSum.get(curr_sum,0)+1
        
        return res


