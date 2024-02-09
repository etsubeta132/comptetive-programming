class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l,r = 0,0
        pdt = 1
        ctr = 0

        if k == 0:
            return 0

        while r < len(nums):

            pdt *= nums[r]

            while pdt >= k and l<=r:
                pdt /= nums[l]
                l+=1
            
            ctr+= r-l+1
            r+=1
        return ctr

