class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        nums.sort()
        
        ctr = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and i<j:
                    if nums[i]+nums[j] < target:
                        ctr+=1
        return ctr