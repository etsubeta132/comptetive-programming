class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        tot = nums[0]
        for i in range(1,len(nums)):
            mx = max(mx,tot)
            tot = max(nums[i],tot+nums[i])

        mx = max(mx,tot)
        return mx

        


