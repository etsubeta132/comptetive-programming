class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        unique = defaultdict(int)
        i = 0
        total = 0
        res = 0
        for j in range(len(nums)):
            rs = nums[j]
            total +=rs
            unique[rs]+=1

            while i< j and unique[rs] > 1:
                unique[nums[i]]-=1
                total-= nums[i]
                i+=1  
            res= max(res,total)
        return res





