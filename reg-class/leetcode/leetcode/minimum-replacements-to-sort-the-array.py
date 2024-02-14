class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        l = 0
        mn = nums[-1]
        ctr =0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < mn:
                mn = nums[i]
            else:
                res = nums[i]/mn
                if nums[i]%mn != 0:
                    res = ceil(nums[i]/mn)
                    mn = min(nums[i]//res,mn)
                ctr+=res-1
        
        return int(ctr)
        

                
