class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums)%p
        print(target)

        if target== 0:
            return 0

        remainder = {0:-1}
        pref = 0
        res = len(nums)
        for i,num in enumerate(nums):
            pref=(num + pref)%p
            key = (pref-target)%p
            if key in remainder:
                res = min(res,i - remainder[key])
                
            remainder[pref] = i
        
        return res if res != len(nums) else -1

                
            