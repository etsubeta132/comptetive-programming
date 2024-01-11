class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l,r = 0,0
        m = len(nums)

        while r < m:

            if nums[r] == 0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
            r+=1
        
        r = l
        while r< m:
            if nums[r] ==1:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
            r+=1

        return nums

        