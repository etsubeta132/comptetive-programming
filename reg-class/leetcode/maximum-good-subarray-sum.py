class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        prefDict = defaultdict(lambda: inf)
        res = -inf
        cur = 0

        for num in nums:
            prefDict[num] = min(cur,prefDict[num])
            cur+=num
           
            if num - k in prefDict:
                res = max(res,cur-prefDict[num-k])
            
            if num + k in prefDict:
                res = max(res,cur-prefDict[num+k])
         
        
        return res if res != -inf else 0
            